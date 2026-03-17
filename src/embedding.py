import os
from dotenv import load_dotenv
from llama_index.embeddings.cohere import CohereEmbedding

load_dotenv()

def get_embedding_model():

    embed_model = CohereEmbedding(
        api_key=os.getenv("COHERE_API_KEY"),
        model_name="embed-english-v3.0"
    )

    return embed_model