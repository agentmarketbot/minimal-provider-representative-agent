import re
from typing import Optional


def find_github_repo_url(text: str) -> Optional[str]:
    """
    Extract the last GitHub repository URL from a text string.

    Args:
        text (str): The text to search for GitHub URLs.

    Returns:
        Optional[str]: The last GitHub repository URL found in the text,
                      or None if no URL is found.

    Example:
        >>> text = "Check this repo https://github.com/user/repo1 and https://github.com/user/repo2"
        >>> find_github_repo_url(text)
        'https://github.com/user/repo2'
    """
    pattern = r"https://github.com/[^\s]+"
    matches = re.findall(pattern, text)
    if matches:
        return matches[-1]
    return None