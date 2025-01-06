class Chunker:
    """
    Chunking class. It is assumed that each record is a tuple (url, description) that we split as one piece.
    """
    def __init__(self, max_chunk_size: int = 500):
        self.max_chunk_size = max_chunk_size  # optional parameter

    def chunk_data(self, data):
        """
        Return list of chunks
        """
        chunks = []
        for url, content in data:
            chunk_text = f"{url}\n{content}"
            # Here we can optionally split if chunk_text exceeds max_chunk_size
            chunks.append(chunk_text)
        return chunks
