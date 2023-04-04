from pydantic import BaseSettings, Field


class EnvironmentVariables(BaseSettings):
    api_key: str = Field(
        "yourapikey",
        description="Your OpenAI API Key",
    )
