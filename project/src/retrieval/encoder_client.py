import os 
from dotenv import load_dotenv
from langchain_gigachat.embeddings import GigaChatEmbeddings

load_dotenv(os.path.abspath(os.path.join('..', '..', '.env')))

GIGACHAT_API_KEY = os.environ["GIGACHAT_API_KEY"]
embedding_client = GigaChatEmbeddings(credentials=GIGACHAT_API_KEY, verify_ssl_certs=False)
