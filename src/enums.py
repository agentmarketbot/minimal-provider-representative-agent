from enum import Enum


class ModelName(str, Enum):
    gpt_4o = "gpt-4o"


class AgentType(str, Enum):
    aider = "aider"
