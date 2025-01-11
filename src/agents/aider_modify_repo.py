"""Module for code review functionality."""

from loguru import logger
import openai


def modify_repo_with_aider(review_command: str) -> str:
    """
    Analyze code and provide review suggestions using OpenAI.

    Args:
        review_command (str): The review instructions

    Returns:
        str: The review suggestions, or None if an error occurs
    """
    try:
        response = openai.chat.completions.create(
            model="o1-mini",
            messages=[{
                "role": "user",
                "content": review_command
            }]
        )
        output = response.choices[0].message.content.strip()
        logger.debug("Review output: {}", output)
        return output

    except Exception as e:
        logger.error("Error generating review: {}", str(e))
        return None