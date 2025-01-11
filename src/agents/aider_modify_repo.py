import io
import os
import shutil
import tempfile
from contextlib import redirect_stderr, redirect_stdout

from aider.coders import Coder
from aider.io import InputOutput
from aider.models import Model
from loguru import logger

from src.utils.git import find_github_repo_url


def modify_repo_with_aider(model_name, solver_command, repo_info=None) -> str:
    io_instance = InputOutput(yes=True)
    model = Model("sonnet")

    output_buffer = io.StringIO()

    temp_dir = tempfile.mkdtemp(prefix="aider_")
    logger.info(f"Created temporary directory: {temp_dir}")

    original_cwd = os.getcwd()

    try:
        with redirect_stdout(output_buffer), redirect_stderr(output_buffer):
            os.chdir(temp_dir)
            logger.info(f"Changed working directory to: {temp_dir}")

            coder = Coder.create(
                main_model=model,
                io=io_instance,
                suggest_shell_commands=True,
                auto_commits=False,
                dirty_commits=False,
                auto_lint=False,
            )

            coder.run(solver_command)

        full_output = output_buffer.getvalue()
        logger.info(f"Full output: {full_output}")

        return full_output

    except Exception as e:
        logger.exception(f"Error during execution: {str(e)}")
        return None

    finally:
        os.chdir(original_cwd)
        logger.info(f"Changed back to original directory: {original_cwd}")

        try:
            shutil.rmtree(temp_dir)
            logger.info(f"Cleaned up temporary directory: {temp_dir}")
        except Exception as e:
            logger.error(f"Error cleaning up temporary directory {temp_dir}: {e}")