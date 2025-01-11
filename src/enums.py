from enum import Enum


class AgentType(str, Enum):
    """Type of agent to use for code review."""
    open_hands = "open-hands"  # Default agent type
    aider = "aider"  # Uses aider-chat for code review
