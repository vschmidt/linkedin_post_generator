from pydantic import BaseModel


class PageContent(BaseModel):
    title: str
    description: str
    example: str
