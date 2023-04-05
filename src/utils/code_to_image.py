import tempfile
from pygments import highlight
from pygments.lexers.python import PythonLexer
from pygments.formatters import ImageFormatter



class CodeToImage:
    def __init__(self, code: str, font_size: int):
        self.code = code
        self.font_size = font_size

    def get_image(self):
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
            lexer = PythonLexer()
            formatter = ImageFormatter(font_size=self.font_size)

            image = highlight(self.code, lexer, formatter)
            f.write(image)
            return f.name
