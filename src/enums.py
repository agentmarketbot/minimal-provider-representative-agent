from enum import Enum


class ModelName(str, Enum):
    gpt_4 = "gpt-4"


class AgentType(str, Enum):
    open_hands = "open-hands"
    aider = "aider"
