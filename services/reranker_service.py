import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class RerankerService:
    """
    A class that implements searching for the closest chunks in the embedding database using the cosine similarity measure.
    """
    def __init__(self, chunks, embeddings):
        """
        :param chunks: list of strings (chunks)
        :param embeddings: list of vectors (embeddings)
        """
        self.chunks = chunks
        self.embeddings = np.array(embeddings)

    def find_top_chunks(self, query_embedding, top_k=3):
        """
        Finds the top_k chunks most similar to query.
        """
        # query_embedding -> [1, embedding_dim]
        query_embedding = np.array(query_embedding).reshape(1, -1)
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]  # similarity vector
        # descending sorting
        top_indices = similarities.argsort()[::-1][:top_k]
        top_results = [(self.chunks[i], similarities[i]) for i in top_indices]
        return top_results
