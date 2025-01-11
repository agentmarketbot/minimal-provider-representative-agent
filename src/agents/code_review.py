"""Module for code review functionality using OpenAI API.
Simplified version that focuses only on generating code review suggestions."""

from loguru import logger
import openai


def generate_code_review(review_command: str) -> str:
    """
    Generate code review suggestions using OpenAI API.

    Args:
        review_command (str): The review instructions or context

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