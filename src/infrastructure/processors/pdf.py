from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import landscape
from reportlab.lib.enums import TA_CENTER

from src.schemes.text import PageContent
from src.utils.code_to_image import CodeToImage


class PagePDFGenerator:
    def __init__(self):
        self.story = []
        self.background_color = "#F0F0F0"
        self.margin = 0.5 * inch

        self.add_styles()

    def add_styles(self):
        self.styles = {}
        self.styles["title"] = ParagraphStyle(
            name="Title", fontSize=36, alignment=TA_CENTER
        )
        self.styles["description"] = ParagraphStyle(
            name="Description", fontSize=12, alignment=TA_CENTER
        )

    def add_cover(self, title):
        title = Paragraph(title, self.styles["title"])
        self.story.append(title)

    def add_back_cover(self):
        pass

    def add_page(self, page: PageContent):
        self.story.append(PageBreak())
        self.story.append(Paragraph(page.title, self.styles["title"]))
        self.story.append(Paragraph(page.description, self.styles["description"]))
        
        self.story.append(PageBreak())
        example_text = Paragraph("Exemplo:", self.styles["title"])
        example_image = Image(CodeToImage(page.example, 15).get_image())
        self.story.append(example_text)
        self.story.append(example_image)

    def generate_pdf(self, file_name):
        doc = SimpleDocTemplate(
            file_name,
            pagesize=landscape((1200, 627)),
            rightMargin=self.margin,
            leftMargin=self.margin,
            topMargin=self.margin,
            bottomMargin=self.margin,
        )

        doc.build(self.story)
