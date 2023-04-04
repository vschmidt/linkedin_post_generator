import re
import json
from typing import List

from src.schemes.text import PageContent


class TextExtractor:
    def __init__(self, text: str) -> None:
        self.text = text
        self.pages = []
        self.extract_pages()

    def extract_pages(self):
        sanitized_pages = self.sanitize_page_text(self.text)
        pages_extracted = json.loads(sanitized_pages)

        for page_extracted in pages_extracted:
            self.pages.append(PageContent(**page_extracted))

    def sanitize_page_text(self, page: str):
        page = page[page.find("[") : page.rfind("]") + 1]
        return re.sub("[\x00-\x1f\x7f-\x9f]", "", page)

    def get_pages(self) -> List[PageContent]:
        return self.pages
