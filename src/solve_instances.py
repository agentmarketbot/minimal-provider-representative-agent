from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Optional

import httpx
import openai
from loguru import logger

from src.agents.aider_modify_repo import modify_repo_with_aider
from src.config import SETTINGS, Settings

TIMEOUT = httpx.Timeout(10.0)
DEFAULT_HEADERS = {"Accept": "application/json"}


@dataclass
class InstanceToSolve:
    """Represents an instance that needs to be solved."""
    instance: dict
    messages_history: Optional[str] = None
    provider_needs_response: bool = False


def _get_instance_details(instance_id: str, settings: Settings) -> Optional[dict]:
    """Fetch instance details from the market API."""
    try:
        headers = {**DEFAULT_HEADERS, "x-api-key": settings.market_api_key}
        url = f"{settings.market_url}/v1/instances/{instance_id}"

        with httpx.Client(timeout=TIMEOUT) as client:
            response = client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        logger.error("Error fetching instance {}: {}", instance_id, str(e))
        return None


def _get_chat_history(instance_id: str, settings: Settings) -> Optional[List[dict]]:
    """Fetch chat history for an instance."""
    try:
        headers = {**DEFAULT_HEADERS, "x-api-key": settings.market_api_key}
        url = f"{settings.market_url}/v1/chat/{instance_id}"

        with httpx.Client(timeout=TIMEOUT) as client:
            response = client.get(url, headers=headers)
            response.raise_for_status()
            chat = response.json()
            
            if isinstance(chat, dict) and chat.get("detail"):
                return None
                
            return sorted(chat, key=lambda m: m["timestamp"]) if chat else []
    except Exception as e:
        logger.error("Error fetching chat history for instance {}: {}", instance_id, str(e))
        return None


def _get_instance_to_solve(instance_id: str, settings: Settings) -> Optional[InstanceToSolve]:
    """
    Get instance details and determine if it needs a response.
    
    Args:
        instance_id: The ID of the instance to check
        settings: Application settings
        
    Returns:
        Optional[InstanceToSolve]: Instance details if it needs solving, None otherwise
    """
    instance = _get_instance_details(instance_id, settings)
    if not instance or instance.get("status") != settings.market_resolved_instance_code:
        return None

    chat_messages = _get_chat_history(instance_id, settings)
    if chat_messages is None:
        return None

    if not chat_messages:
        return InstanceToSolve(instance=instance)

    # Check if we need to respond (provider's message and under 20 messages)
    last_message = chat_messages[-1]
    provider_needs_response = last_message["sender"] == "provider" and len(chat_messages) < 20

    messages_history = "\n\n".join(
        [f"{msg['sender']}: {msg['message']}" for msg in chat_messages]
    )

    return InstanceToSolve(
        instance=instance,
        messages_history=messages_history,
        provider_needs_response=provider_needs_response,
    )


def _clean_response(response: str, conversation_history: Optional[str] = None) -> str:
    """Clean and format the AI response."""
    if not response:
        return "NO_RESPONSE_NEEDED"

    try:
        prompt = """
        Review this code review response and previous conversation.
        Extract only NEW technical improvements or changes that haven't been mentioned.
        Focus on code changes and technical suggestions.
        Format them clearly and concisely.
        
        If no new technical suggestions, respond with 'NO_RESPONSE_NEEDED'.
        
        Previous conversation:
        {history}
        
        Current response:
        {feedback}
        """

        cleaned = openai.chat.completions.create(
            model="o1-mini",
            messages=[{
                "role": "user",
                "content": prompt.format(
                    feedback=response,
                    history=conversation_history or "No previous conversation"
                )
            }]
        )
        return cleaned.choices[0].message.content.strip()

    except Exception as e:
        logger.error("Error cleaning response: {}", str(e))
        return response


def _solve_instance(instance_to_solve: InstanceToSolve) -> Optional[str]:
    """
    Generate a solution for the given instance.
    
    Args:
        instance_to_solve: Instance details and chat history
        
    Returns:
        Optional[str]: The solution message to send, or None if no response needed
    """
    instance_id = instance_to_solve.instance["id"]
    logger.info("Solving instance: {}", instance_id)

    try:
        # Extract PR and issue links from chat history
        pr_url = None
        issue_url = None
        if instance_to_solve.messages_history:
            import re
            pr_match = re.search(r"https://github\.com/[^/]+/[^/]+/pull/\d+", 
                               instance_to_solve.messages_history)
            if pr_match:
                pr_url = pr_match.group(0)
                
                # Try to find related issue
                pr_response = httpx.get(pr_url, timeout=TIMEOUT)
                if pr_response.status_code == 200:
                    issue_match = re.search(
                        r"https://github\.com/[^/]+/[^/]+/issues/\d+",
                        pr_response.text
                    )
                    if issue_match:
                        issue_url = issue_match.group(0)

        # Prepare review command
        review_command = (
            "You are reviewing a PR. Provide specific technical suggestions "
            "or respond to questions. Reply 'NO_RESPONSE_NEEDED' if no changes needed."
        )
        if pr_url:
            review_command += f"\nPR: {pr_url}"
        if issue_url:
            review_command += f"\nRelated issue: {issue_url}"

        # Get AI response
        response = modify_repo_with_aider(review_command)
        if not response:
            logger.warning("Empty response from AI")
            return None

        # Clean and validate response
        cleaned = _clean_response(response, instance_to_solve.messages_history)
        return None if cleaned == "NO_RESPONSE_NEEDED" else cleaned

    except Exception as e:
        logger.error("Error solving instance {}: {}", instance_id, str(e))
        return None


def _get_awarded_proposals(settings: Settings) -> List[dict]:
    """Get recently awarded proposals from the last 24 hours."""
    try:
        headers = {**DEFAULT_HEADERS, "x-api-key": settings.market_api_key}
        url = f"{settings.market_url}/v1/proposals/"

        with httpx.Client(timeout=TIMEOUT) as client:
            response = client.get(url, headers=headers)
            response.raise_for_status()
            proposals = response.json()

        # Filter for awarded proposals from last 24 hours
        cutoff = datetime.utcnow() - timedelta(days=1)
        return [
            p for p in proposals
            if p["status"] == settings.market_awarded_proposal_code
            and datetime.fromisoformat(p["creation_date"]) > cutoff
        ]

    except Exception as e:
        logger.error("Error fetching awarded proposals: {}", str(e))
        return []


def _send_message(instance_id: str, message: str, settings: Settings) -> bool:
    """Send a message to an instance chat."""
    try:
        headers = {**DEFAULT_HEADERS, "x-api-key": settings.market_api_key}
        url = f"{settings.market_url}/v1/chat/send-message/{instance_id}"
        
        with httpx.Client(timeout=TIMEOUT) as client:
            response = client.post(url, headers=headers, json={"message": message})
            response.raise_for_status()
            return True

    except Exception as e:
        logger.error("Error sending message to instance {}: {}", instance_id, str(e))
        return False


def solve_instances_handler() -> None:
    """
    Main handler for solving instances. This function:
    1. Fetches recently awarded proposals
    2. Checks each instance for required responses
    3. Generates and sends solutions where needed
    """
    try:
        logger.info("Starting solve instances handler")
        awarded_proposals = _get_awarded_proposals(SETTINGS)

        if not awarded_proposals:
            logger.debug("No awarded proposals found")
            return

        logger.info("Found {} awarded proposals", len(awarded_proposals))

        for proposal in awarded_proposals:
            instance_to_solve = _get_instance_to_solve(proposal["instance_id"], SETTINGS)
            if not instance_to_solve or not instance_to_solve.provider_needs_response:
                continue

            message = _solve_instance(instance_to_solve)
            if message and _send_message(instance_to_solve.instance["id"], message, SETTINGS):
                logger.info("Successfully processed instance {}", instance_to_solve.instance["id"])

    except Exception as e:
        logger.error("Fatal error in solve instances handler: {}", str(e))
