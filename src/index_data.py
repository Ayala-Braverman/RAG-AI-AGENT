from llama_index.core import VectorStoreIndex
from chunk_data import chunk_documents
from load_data import load_documents
from embedding import get_embedding_model


def create_index():

    docs = load_documents()

    nodes = chunk_documents(docs)

    embed_model = get_embedding_model()

    index = VectorStoreIndex(
        nodes,
        embed_model=embed_model
    )

    return index


if __name__ == "__main__":

    index = create_index()

    print("Index created successfully")

    query_engine = index.as_query_engine()

    response = query_engine.query("Which database was chosen for the system?")

    print("\nAnswer:")
    print(response)