from typing import List
from src.llm.llm_client import llm_client
from src.retrieval.encoder_client import embedding_client
from src.prompts.topic_prompt import EXTRACT_TOPIC_SYSTEM_PROMPT


def get_topic(text: str) -> List[str]:
    """
    Получение темы (топика) запроса для первичной фильтрации по БД.
    """

    message = [
        {'role': 'system', 'content': EXTRACT_TOPIC_SYSTEM_PROMPT},
        {'role': 'user', 'content': text}
    ]

    topic = llm_client.chat.completions.create(
        model="deepseek-chat",
        messages=message,
        stream=False
    ).choices[0].message.content

    return topic.lower()


def get_embeddings(texts: List[str]) -> List[dict]:
    """
    Получение эмбеддинга текстов.
    """

    embeddings = embedding_client.embed_documents(texts)

    return embeddings
