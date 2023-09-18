import os
import configparser
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

def read_key():
    # Get the absolute path to the configuration file
    config_file_path = os.path.join(os.path.dirname(__file__), 'source', 'api', 'utils', 'config.ini')

    # Initialize the configparser
    config = configparser.ConfigParser()

    # Read the configuration file using the absolute file path
    config.read(config_file_path)

    openai.api_key = os.getenv('OPENAI_API_KEY')

    # Get the API key from the configuration file
    print(os.getenv('OPENAI_API_KEY'))

# Call the function to read the API key
read_key()