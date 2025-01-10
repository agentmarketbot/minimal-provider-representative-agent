import os
import re
import shutil
from typing import Optional

import git
from loguru import logger


def find_github_repo_url(text: str) -> Optional[str]:
    pattern = r"https://github.com/[^\s]+"
    matches = re.findall(pattern, text)
    if matches:
        return matches[-1]
    return None


def clone_repository(repo_url: str, target_dir: str) -> None:
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)

    os.makedirs(target_dir)
    git.Repo.clone_from(repo_url, target_dir)
    logger.info(f"Cloned repository from {repo_url} to {target_dir}")