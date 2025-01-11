from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Required settings
    openai_api_key: str = Field(..., description="OpenAI API key for code review")
    market_api_key: str = Field(..., description="Agent Market API key")

    # Optional settings with defaults
    market_url: str = Field("https://api.agent.market", description="Agent Market API URL")
    max_bid: float = Field(0.01, gt=0, description="Maximum bid for proposals")

    # Market status codes
    market_open_instance_code: int = Field(0, description="Code for open instances")
    market_resolved_instance_code: int = Field(3, description="Code for resolved instances")
    market_awarded_proposal_code: int = Field(1, description="Code for awarded proposals")

    class Config:
        case_sensitive = False

SETTINGS = Settings.load_settings()