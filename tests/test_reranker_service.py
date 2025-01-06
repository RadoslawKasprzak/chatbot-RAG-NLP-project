import pytest
import numpy as np
from services.reranker_service import RerankerService

def test_find_top_chunks():
    chunks = ["C1", "C2", "C3"]
    embeddings = np.array([
        [1.0, 0.0],  # e.g. C1
        [0.0, 1.0],  # C2
        [0.7, 0.7],  # C3
    ])
    reranker = RerankerService(chunks, embeddings)

    query_embedding = [0.9, 0.9]  # closer to C3
    top_results = reranker.find_top_chunks(query_embedding, top_k=2)

    # top1 should be C3, top2 one of C1 or C2
    assert len(top_results) == 2
    assert top_results[0][0] == "C3"
