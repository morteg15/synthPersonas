import os
import configparser


def read_key():
    # Initialize the configparser
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read('source\\api\\utils\\config.ini')

    # Get the API key from the configuration file
    api_key = config['OpenAI']['API_KEY']

    # Set the API key as an environment variable
    os.environ['OPENAI_API_KEY'] = api_key

    # Now you can use os.getenv("OPENAI_API_KEY") to get the API key
    print(os.getenv("OPENAI_API_KEY"))
