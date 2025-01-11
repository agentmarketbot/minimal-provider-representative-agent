"""Module for interacting with the Aider code review tool."""

import io
from contextlib import redirect_stderr, redirect_stdout

from aider.coders import Coder
from aider.io import InputOutput
from aider.models import Model
from loguru import logger


def modify_repo_with_aider(review_command: str) -> str:
    """
    Use Aider to analyze code and provide review suggestions.

    Args:
        review_command (str): The review instructions for Aider

    Returns:
        str: The review suggestions from Aider, or None if an error occurs
    """
    try:
        # Configure Aider
        io_instance = InputOutput(yes=True)  # Auto-confirm any prompts
        model = Model("sonnet")  # Use the default model
        output_buffer = io.StringIO()

        # Capture Aider's output
        with redirect_stdout(output_buffer), redirect_stderr(output_buffer):
            coder = Coder.create(
                main_model=model,
                io=io_instance,
                suggest_shell_commands=False,  # Disable shell commands for security
                auto_commits=False,  # Disable auto-commits
                dirty_commits=False,
                auto_lint=False,
            )
            coder.run(review_command)

        # Extract and return the review suggestions
        output = output_buffer.getvalue()
        logger.debug("Aider output: {}", output)
        return output

    except Exception as e:
        logger.error("Error running Aider: {}", str(e))
        return None