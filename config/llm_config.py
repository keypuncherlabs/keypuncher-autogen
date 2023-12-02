import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

open_ai_config_list = [
    {
        'model': 'gpt-4-1106-preview',
        'api_key': openai_api_key
    }
]

llm_config = {
    'request_timeout': 400,
    'seed': 41,
    'config_list': open_ai_config_list,
    'temperature': 0
}
