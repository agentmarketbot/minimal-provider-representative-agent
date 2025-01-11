import asyncio
from typing import List, Optional, Set

import httpx
from loguru import logger

from src.config import SETTINGS, Settings

TIMEOUT = httpx.Timeout(10.0)
DEFAULT_HEADERS = {"Accept": "application/json"}


async def _create_proposal_for_instance(instance: dict, settings: Settings) -> bool:
    """
    Create a proposal for a given market instance.

    Args:
        instance (dict): The instance data from the market API
        settings (Settings): Application settings

    Returns:
        bool: True if proposal was created successfully, False otherwise
    """
    instance_id = instance["id"]

    try:
        logger.info("Creating proposal for instance: {}", instance_id)
        headers = {**DEFAULT_HEADERS, "x-api-key": settings.market_api_key}
        url = f"{settings.market_url}/v1/proposals/create/for-instance/{instance_id}"
        data = {"max_bid": settings.max_bid}

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=data)
            response.raise_for_status()

        logger.info("Proposal created successfully for instance: {}", instance_id)
        return True

    except httpx.HTTPError as e:
        logger.error("HTTP error creating proposal for instance {}: {}", instance_id, str(e))
        return False
    except Exception as e:
        logger.error("Error creating proposal for instance {}: {}", instance_id, str(e))
        return False


async def _get_open_instances(settings: Settings) -> Optional[List[dict]]:
    """Fetch open instances from the market API."""
    try:
        headers = {**DEFAULT_HEADERS, "x-api-key": settings.market_api_key}
        url = f"{settings.market_url}/v1/instances/"
        params = {"instance_status": settings.market_open_instance_code}

        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()

    except Exception as e:
        logger.error("Error fetching open instances: {}", str(e))
        return None


async def _get_existing_proposals(settings: Settings) -> Set[str]:
    """Fetch existing proposals and return their instance IDs."""
    try:
        headers = {**DEFAULT_HEADERS, "x-api-key": settings.market_api_key}
        url = f"{settings.market_url}/v1/proposals/"

        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            proposals = response.json()
            return {proposal["instance_id"] for proposal in proposals}

    except Exception as e:
        logger.error("Error fetching existing proposals: {}", str(e))
        return set()


async def async_market_scan_handler() -> None:
    """
    Scan the market for open instances and create proposals.
    
    This handler:
    1. Fetches open instances from the market
    2. Fetches existing proposals to avoid duplicates
    3. Creates new proposals for instances without existing proposals
    """
    open_instances = await _get_open_instances(SETTINGS)
    if not open_instances:
        logger.debug("No open instances found")
        return

    logger.debug("Found {} open instances", len(open_instances))
    filled_instances = await _get_existing_proposals(SETTINGS)

    # Create proposals for instances that don't have one yet
    tasks = [
        _create_proposal_for_instance(instance, SETTINGS)
        for instance in open_instances
        if instance["id"] not in filled_instances
    ]
    
    if tasks:
        results = await asyncio.gather(*tasks)
        successful = sum(1 for r in results if r)
        logger.info("Created {} new proposals", successful)


def market_scan_handler() -> None:
    """Entry point for the market scanning functionality."""
    try:
        asyncio.run(async_market_scan_handler())
    except Exception as e:
        logger.error("Fatal error in market scan handler: {}", str(e))
