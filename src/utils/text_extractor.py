import json
import re
from typing import List

from src.schemes.text import PageContent


class TextExtractor:
    def __init__(self, text: str) -> None:
        self.text = text
        self.pages = []
        self.extract_pages()

    def extract_pages(self):
        pattern = r'\{.*?"title":\s*"(.*?)",\s*"description":\s*"(.*?)",\s*"example":\s*"(.*?)".*?\}'

        for match in re.finditer(pattern, self.text, re.DOTALL):
            page_extracted = {
                "title": match.group(1),
                "description": match.group(2),
                "example": match.group(3),
            }
            self.pages.append(PageContent(**page_extracted))

    def get_pages(self) -> List[PageContent]:
        return self.pages
