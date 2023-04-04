from src.infrastructure.openai.text_generator import OpenAITextGenerator
from src.settings.environment import EnvironmentVariables
from src.settings.app import AppVariables
from src.utils.text_extractor import TextExtractor
from src.infrastructure.processors.pdf import PagePDFGenerator

# Configurações
app_variables = AppVariables()
env_variables = EnvironmentVariables()

# Gerando o texto
prompt = 'Faça para mim um artigo para o linkedin com 2 páginas sobre o tema datetime em Python com as seguintes regras:\n* Gere um texto com exemplos de código para cada página\n* Sua resposta deve ser um json válido\n* Não devem haver quebras de linha\n* A sua resposta deve conter apenas objetos no seguinte formato: [{"title": <coloque o titulo da página> ,"description": <coloque a descrição da página> ,"example": "<coloque o exemplo da página>"}, ...]'
chatgpt = OpenAITextGenerator(api_key=env_variables.api_key)

results = chatgpt.generate_text(prompt)

# Processamento do texto
text_extractor = TextExtractor(results)
pages_content = text_extractor.get_pages()

# Gerar páginas PDF
pdf_file = PagePDFGenerator()

pdf_file.add_cover()

for page_content in pages_content:
    pdf_file.add_page(page_content)

pdf_file.add_back_cover()

pdf_file.generate_pdf("outputs/publicação.pdf")
