from copy import deepcopy
from datetime import date
from functools import partial

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    Frame,
    Image,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

from src.schemes.text import PageContent
from src.utils.code_to_image import CodeToImage


class PagePDFGenerator:
    def __init__(self):
        self.story = []

        self.margin = 20 * mm
        self.page_width, self.page_height = landscape((1200, 627))

        self.__generate_text_styles()

    def __generate_text_styles(self):
        styles = getSampleStyleSheet()

        self.header_title_style = deepcopy(styles["Title"])
        self.header_title_style.textColor = "#ffffff"
        self.header_title_style.alignment = TA_LEFT

        self.main_title_style = deepcopy(styles["Title"])
        self.main_title_style.alignment = TA_CENTER
        self.main_title_style.textColor = "#ffffff"
        self.main_title_style.fontSize = 40

        self.main_description_style = deepcopy(styles["Heading1"])
        self.main_description_style.alignment = TA_CENTER
        self.main_description_style.textColor = "#ffffff"
        self.main_description_style.spaceBefore = 60
        self.main_description_style.fontSize = 28
        self.main_description_style.leading = 40

        self.subtitle_style = styles["Heading1"]
        self.subtitle_style.textColor = "#ffffff"
        self.subtitle_style.alignment = TA_RIGHT

    def add_cover(self, title):
        self.story.append(NextPageTemplate("cover_template"))
        spacer = Spacer(0, self.page_height / 2 - self.main_title_style.fontSize)
        title = Paragraph(title, style=self.main_title_style)

        self.story.append(spacer)
        self.story.append(title)

    def add_back_cover(self):
        self.story.append(NextPageTemplate("backcover_template"))
        self.story.append(PageBreak())
        spacer = Spacer(0, self.page_height / 2 - self.main_title_style.fontSize)
        title = Paragraph("FIM <3", style=self.main_title_style)

        self.story.append(spacer)
        self.story.append(title)

    def add_page(self, page: PageContent):
        self.story.append(NextPageTemplate("content_template"))
        self.story.append(PageBreak())
        self.story.append(Paragraph(page.title, self.main_title_style))
        self.story.append(Paragraph(page.description, self.main_description_style))

        self.story.append(NextPageTemplate("content_template"))
        self.story.append(PageBreak())
        example_text = Paragraph("Exemplo:", self.main_title_style)
        spacer = Spacer(0, 40)
        example_image = Image(CodeToImage(page.example, 15).get_image())

        self.story.append(example_text)
        self.story.append(spacer)
        self.story.append(example_image)

    def generate_pdf(self, file_name):
        doc = SimpleDocTemplate(
            file_name,
            pagesize=(self.page_width, self.page_height),
            rightMargin=self.margin,
            leftMargin=self.margin,
            topMargin=self.margin,
            bottomMargin=self.margin,
        )

        frame = Frame(
            doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal"
        )

        header_content = Paragraph(f"Gerado em {date.today()}", self.header_title_style)
        footer_content = Paragraph(
            "Feito pelo Schmidt e sua nova ferramenta CHATGPT",
            self.main_description_style,
        )

        cover_template = PageTemplate(
            id="cover_template",
            frames=frame,
            onPage=partial(
                self.layout_cover_template,
                header_content=header_content,
                footer_content=footer_content,
                background_color="#007bff",
            ),
        )

        content_template = PageTemplate(
            id="content_template",
            frames=frame,
            onPage=partial(
                self.layout_content_template,
                background_color="#007bff",
            ),
        )

        backcover_template = PageTemplate(
            id="backcover_template",
            frames=frame,
            onPage=partial(
                self.layout_content_template,
                background_color="#007bff",
            ),
        )

        doc.addPageTemplates([cover_template, content_template, backcover_template])
        doc.build(self.story)

    def layout_content_template(self, canvas, doc, background_color):
        self.__fill_background(canvas, background_color)

    def layout_cover_template(
        self, canvas, doc, header_content, footer_content, background_color
    ):
        self.__fill_background(canvas, background_color)
        self.__add_header(canvas, doc, header_content)
        self.__add_footer(canvas, doc, footer_content)

    def __fill_background(self, canvas, color):
        canvas.saveState()
        canvas.setFillColor(HexColor(color))
        canvas.rect(0, 0, self.page_width, self.page_height, fill=1)
        canvas.restoreState()

    def __add_header(self, canvas, doc, content):
        canvas.saveState()
        w, h = content.wrap(doc.width, doc.topMargin)
        content.drawOn(
            canvas, doc.leftMargin, doc.height + doc.bottomMargin + doc.topMargin - h
        )
        canvas.restoreState()

    def __add_footer(self, canvas, doc, content):
        canvas.saveState()
        w, h = content.wrap(doc.width, doc.bottomMargin)
        content.drawOn(canvas, doc.leftMargin, h)
        canvas.restoreState()
