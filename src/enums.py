from enum import Enum


class ModelName(str, Enum):
    gpt_4_turbo = "gpt-4-turbo"


class AgentType(str, Enum):
    open_hands = "open-hands"
    aider = "aider"
