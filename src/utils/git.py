import re
from typing import Optional


def find_github_repo_url(text: str) -> Optional[str]:
    pattern = r"https://github.com/[^\s]+"
    matches = re.findall(pattern, text)
    if matches:
        return matches[-1]
    return None