from langchain_text_splitters import RecursiveCharacterTextSplitter

with open("data/unprocessed/basement_layout.txt", encoding="utf-8") as f:
    state_of_the_union = f.read()
sections = state_of_the_union.strip().split("\n\n")
texts = [section for section in sections]
