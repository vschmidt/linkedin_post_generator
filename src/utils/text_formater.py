from pygments.lexers.python import PythonLexer
from pygments.token import Token
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph


class PygmentsCodeColoredText:
    def __init__(self, text):
        self.text = text
        self.colors = {
            Token.Keyword: "#D73A49",  # Palavras-chave
            Token.Name.Builtin: "#6F42C1",  # Funções built-in
            Token.Name.Namespace: "#6F42C1",  # Módulos e pacotes
            Token.Name.Variable: "#005CC5",  # Variáveis
            Token.Operator: "#018786",  # Operadores
            Token.Comment: "#6A737D",  # Comentários
            Token.Literal.String: "#28A745",  # Strings
            Token.Text.Whitespace: "#ffffff",  # Quebras de linha
        }

    def _generate_paragraph(self):
        """
        Gera o parágrafo com as cores definidas
        """
        paragraph_style = ParagraphStyle(
            name="Code",
            fontName="Courier",
            fontSize=10,
            leading=10,
            leftIndent=inch / 4,
            rightIndent=inch / 4,
            textColor=HexColor("#000000"),
            alignment=TA_LEFT,
        )

        html_code = self._highlight()

        return Paragraph(html_code, style=paragraph_style)

    def _highlight(self):
        """
        Realiza o highlight do código com o Pygments
        """
        lexer = PythonLexer()

        html = ""
        for line in self.text.split("\n"):
            # Gerar os tokens de acordo com a frase e o lexer
            tokens = list(lexer.get_tokens(line))

            # Percorrer cada token e escrever na posição correta com a cor apropriada
            for token_type, token_text in tokens:
                if token_text == "\n":
                    html += "<br/>"
                elif token_text.isspace():
                    html += "&nbsp" * len(token_text)
                else:
                    color = self.colors.get(token_type, "#000000")
                    html += f'<font color="{color}">{token_text}</font>'

        return html
