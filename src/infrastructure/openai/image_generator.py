from io import BytesIO

import openai
import requests
from PIL import Image


class DALLEImageGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_image(self, description, size):
        response = openai.Image.create(prompt=description, n=1, size=size)

        image_url = response["data"][0]["url"]
        image_data = BytesIO(requests.get(image_url).content)
        image = Image.open(image_data)
        return image

    def save_image(self, image, filename):
        image.save(filename)
