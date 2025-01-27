import chromadb
import os
from typing import List, Optional, Dict

CHROMA_DATA_PATH = os.path.abspath("src/chroma")
COLLECTION_NAME = "news_embeddings"
client = chromadb.PersistentClient(CHROMA_DATA_PATH)
collection = client.get_collection(COLLECTION_NAME)


def search_similarity_chunk(embedding: List[list], filters_kwargs: Optional[Dict[str, str]] = None, top_k: int = 10) -> List[list]:
    """
    Поиск наиболее релевантных текстов из БД.
    """

    if filters_kwargs is not None:

        results = collection.query(
            query_embeddings=embedding,
            where={"topic": {"$eq": filters_kwargs["topic"]}},
            n_results=top_k
        )
    else:
        results = collection.query(
            query_embeddings=embedding,
            n_results=top_k
        )

    return results["documents"]
