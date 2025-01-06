import pytest
from unittest.mock import patch
from services.embedding_service import EmbeddingService

@patch("services.embedding_service.openai.Embedding.create")
def test_get_embedding_single_text(mock_openai):
    # Symulacja zwrotki z openai
    mock_openai.return_value = {
        "data": [
            {"embedding": [0.1, 0.2, 0.3]}
        ]
    }

    svc = EmbeddingService(model_name="test-model")
    embedding = svc.get_embedding("Hello world")

    assert len(embedding) == 3
    assert embedding == [0.1, 0.2, 0.3]
    mock_openai.assert_called_once()
