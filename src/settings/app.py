from pydantic import BaseSettings, Field


class AppVariables(BaseSettings):
    post_topic: str = Field("datetime em Python", description="Your post topic")
    number_of_pages: int = Field(2, description="Number of pages in post")
