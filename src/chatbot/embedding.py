from langchain_huggingface import HuggingFaceEmbeddings

### Creating embeddings from chunks of text
with open("data/unprocessed/basement_layout.txt", encoding="utf-8") as f:
    state_of_the_union = f.read()
sections = state_of_the_union.strip().split("\n\n")
texts = [section for section in sections]


def get_embedding_function():

    embeddings= HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    # embeddings = embeddings_model.embed_documents(texts)
    return embeddings

# embeddings = [ (embedding, {"chunk_id", i})for i, embedding in enumerate(embeddings)]
# print(texts)