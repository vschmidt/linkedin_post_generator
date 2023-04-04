from pydantic import BaseSettings, Field


class AppVariables(BaseSettings):
    post_topic: str = Field("try-except em Python", description="Your post topic")
    number_of_pages: int = Field(2, description="Number of pages in post")
    base_colors: str = Field(
        "#0077c2 #1dcaff #2c98f0 #3498db", description="Colors used in post"
    )
