import os
import certifi

# תיקון בעיית SSL (חשוב מאוד ב-Windows)
os.environ["SSL_CERT_FILE"] = certifi.where()

from dotenv import load_dotenv
load_dotenv()

from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.pinecone import PineconeVectorStore

from pinecone import Pinecone

from load_data import load_documents
from chunk_data import chunk_documents
from embedding import get_embedding_model


def create_pinecone_index():

    # התחברות ל-Pinecone
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

    # שם ה-index שיצרת
    pinecone_index = pc.Index("rag-docs")

    # טעינת נתונים
    docs = load_documents()

    # Chunking
    nodes = chunk_documents(docs)

    # מודל embeddings (Cohere)
    embed_model = get_embedding_model()

    # יצירת Vector Store
    vector_store = PineconeVectorStore(pinecone_index=pinecone_index)

    # Storage Context
    storage_context = StorageContext.from_defaults(
        vector_store=vector_store
    )

    # יצירת האינדקס (מעלה ל-Pinecone)
    index = VectorStoreIndex(
        nodes,
        storage_context=storage_context,
        embed_model=embed_model
    )

    return index


if __name__ == "__main__":

    print("Starting upload to Pinecone...")

    index = create_pinecone_index()

    print("\nDocuments uploaded to Pinecone")

    # יצירת query engine
    query_engine = index.as_query_engine()

    # בדיקת שאילתה
    response = query_engine.query(
        "What database does the system use?"
    )

    print("\nAnswer:")
    print(response)