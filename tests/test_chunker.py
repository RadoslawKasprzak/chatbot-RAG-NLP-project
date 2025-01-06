import pytest
from models.chunker import Chunker

def test_chunker_basic():
    data = [("http://example.com", "Opis testowy"), ("http://foo.com", "Treść foo")]
    chunker = Chunker(max_chunk_size=50)
    chunks = chunker.chunk_data(data)

    assert len(chunks) == 2
    assert "http://example.com" in chunks[0]
    assert "Opis testowy" in chunks[0]
