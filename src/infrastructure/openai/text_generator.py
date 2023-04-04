import openai


class OpenAITextGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_text(self, prompt):
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
        )

        message = completions.choices[0].text
        return message
