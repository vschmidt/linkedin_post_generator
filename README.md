# LinkedIn Post Generator

This is a simple project that generates LinkedIn posts using GPT-3. It was developed by vschmidt.

## Installation

To use this project, you will need to have access to the OpenAI GPT-3 API. You will also need to install the following packages:

- **pipenv**

Once you have installed these packages, you can clone the repository to your local machine:

```bash
$ git clone https://github.com/vschmidt/linkedin_post_generator.git
```

And install other requirements:

```bash
$ pipenv install
```

## Usage

To use the LinkedIn Post Generator, you will need to set up a **src/settings/environment** file with your OpenAI API key.

Once you have set up your API key, you can run the main.py script to generate a LinkedIn post. The script will prompt you for a topic, and then generate a post based on that topic.

```bash
python main.py
```

The generated files will be copied to **outputs/** folder.

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the AGPL License. See the LICENSE file for details.
