import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(os.path.join('.env'))

LLM_API_KEY = os.environ["DEEPSEEK_API_KEY"]
LLM_BASE_URL = "https://api.deepseek.com"

llm_client = OpenAI(
    api_key=LLM_API_KEY,
    base_url=LLM_BASE_URL
)
