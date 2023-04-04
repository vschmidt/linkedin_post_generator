from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

from src.schemes.text import PageContent
from src.utils.text_formater import PygmentsCodeColoredText


class PagePDFGenerator:
    def __init__(self):
        self.story = []
        self.background_color = '#F0F0F0'
        self.margin = 0.5*inch
        self.styles = getSampleStyleSheet()

    def add_cover(self, title):
        title = Paragraph(title)
        self.story.append(title)

    def add_back_cover(self):
        pass

    def add_page(self, page: PageContent):
        self.story.append(PageBreak())
        title = Paragraph(page.title, self.styles["Heading1"])       
        self.story.append(title)
        description = Paragraph(page.description, self.styles["Normal"])
        self.story.append(description)

        self.story.append(PageBreak())
        example_text = Paragraph("Exemplo:", self.styles["Normal"])        
        example_code = PygmentsCodeColoredText(page.example)._generate_paragraph()   

        self.story.append(example_text)
        self.story.append(example_code)

    def generate_pdf(self, file_name):
        doc = SimpleDocTemplate(
            file_name,
            pagesize=letter,
            rightMargin=self.margin,
            leftMargin=self.margin,
            topMargin=self.margin,
            bottomMargin=self.margin,
        )

        doc.build(self.story)
