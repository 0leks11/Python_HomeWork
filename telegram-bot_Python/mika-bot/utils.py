import os
from dotenv import load_dotenv

def load_env_variables():
    load_dotenv()
    return {
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
        'TELEGRAM_TOKEN': os.getenv('TELEGRAM_TOKEN'),
        'REDIS_URL': os.getenv('REDIS_URL'),
    }