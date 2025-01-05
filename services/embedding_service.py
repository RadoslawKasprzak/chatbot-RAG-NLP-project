import os
import openai

class EmbeddingService:
    """
    Class for generating embeddings with OpenAI.
    """
    def __init__(self, model_name: str = "text-embedding-ada-002"):
        self.model_name = model_name
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def get_embedding(self, text: str):
        """
        Gets the embedding for a single text.
        """
        response = openai.Embedding.create(
            input=text,
            model=self.model_name
        )
        embedding = response["data"][0]["embedding"]
        return embedding

    def get_embeddings(self, texts: list):
        """
        Gets the embedding for a list of text.
        """
        response = openai.Embedding.create(
            input=texts,
            model=self.model_name
        )
        embeddings = [r["embedding"] for r in response["data"]]
        return embeddings
