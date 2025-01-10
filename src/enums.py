from enum import Enum


class ModelName(str, Enum):
    gpt_4o = "gpt-4o"
    gpt_4o_mini = "gpt-4o-mini"


class AgentType(str, Enum):
    open_hands = "open-hands"
    aider = "aider"
    raaid = "raaid"
