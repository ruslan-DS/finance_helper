from datetime import date
from src.retrieval.embeddings import get_topic, get_embeddings
from src.retrieval.similarity import search_similarity_chunk


def launch_retrieval(query: str, select_date: date) -> str:
    """
    Функция запуска retrieval для поиска релевантной информации
    select_date: while unuse
    """

    topic = get_topic(query)
    embedding = get_embeddings([query])

    filters_kwargs = {"topic": topic}
    similarity_chunks = search_similarity_chunk(embedding, filters_kwargs)

    context = "\n\n".join([f"КОНТЕКСТ №{idx}:\n{chunk}" for idx, chunk in enumerate(similarity_chunks[0], 1)])

    return context
