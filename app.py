import streamlit as st
import os
from dotenv import load_dotenv

# import services
from services.data_loader import DataLoader
from services.embedding_service import EmbeddingService
from services.reranker_service import RerankerService
from services.chat_service import ChatService

# import chunker
from models.chunker import Chunker

def main():
    # load environment variables (e.g. OpenAI key)
    load_dotenv()

    st.title("Asystent studenta PW")

    # Initialize storage in st.session_state
    # 1) 'ready' -> whether the application loaded correctly
    # 2) 'chunks', 'chunk_embeddings' -> stored data and embeddings
    # 3) 'reranker', 'chat_service' -> initialized objects
    # 4) 'debug_logs' -> log array for debugging

    if 'ready' not in st.session_state:
        st.session_state['ready'] = False
        st.session_state['debug_logs'] = []  # debug logs

        # loading data from the file
        data_loader = DataLoader(data_file_path="data/data.txt")
        data = data_loader.load_data()

        # chunking data
        chunker = Chunker()
        chunks = chunker.chunk_data(data)

        # generating embeddings for chunks
        embed_service = EmbeddingService()
        chunk_embeddings = embed_service.get_embeddings(chunks)

        # reranker object
        reranker = RerankerService(chunks, chunk_embeddings)

        # ChatService
        chat_service = ChatService()

        # save to st.session_state so as not to create it on every refresh
        st.session_state['chunks'] = chunks
        st.session_state['chunk_embeddings'] = chunk_embeddings
        st.session_state['reranker'] = reranker
        st.session_state['chat_service'] = chat_service
        st.session_state['ready'] = True

    # CheckBox to enable/disable debugging
    debug_mode = st.checkbox("Pokaż logi debugowania")

    if st.session_state['ready']:
        user_query = st.text_input("Zadaj pytanie:", value="")
        if st.button("Wyślij"):
            if user_query.strip():
                #1. Get query embedding
                embed_service = EmbeddingService()
                query_embedding = embed_service.get_embedding(user_query)
                
                # Add logs
                st.session_state['debug_logs'].append(
                    f"[INFO] Wygenerowano embedding zapytania dla tekstu: '{user_query[:50]}...' (długość: {len(user_query)})"
                )

                #2. Find the most similar chunks
                reranker = st.session_state['reranker']
                top_chunks = reranker.find_top_chunks(query_embedding, top_k=3)

                # Build information about which chunks were selected
                chunks_log = []
                for idx, (chunk_text, similarity) in enumerate(top_chunks):
                    # shorten chunk_text to first ~500 characters to not fill the log
                    short_chunk = (chunk_text[:500] + '...') if len(chunk_text) > 500 else chunk_text
                    chunks_log.append(f"#{idx+1} similarity={similarity:.3f} -> '{short_chunk}'")
                
                # Log entry
                st.session_state['debug_logs'].append(
                    "[INFO] Wybrano top_k chunków:\n" + "\n".join(chunks_log)
                )

                # 3. Build the context (e.g. we concatenate top_chunks into one string)
                context_text = "\n".join([f"Chunk: {tc[0]} (similarity: {tc[1]:.3f})" for tc in top_chunks])

                #4. Invoke ChatGPT with context
                chat_service = st.session_state['chat_service']
                response = chat_service.get_chat_response(context_text, user_query)

                #  Add to logs:
                st.session_state['debug_logs'].append(
                    f"[INFO] Odpowiedź ChatGPT:\n{response}"
                )

                # 5. View Reply
                st.write("**Odpowiedź:**")
                st.write(response)

    # Display logs if checkbox debug_mode == True
    if debug_mode:
        st.subheader("Logi debugowania")
        # Display all logs
        for log_entry in st.session_state['debug_logs']:
            st.text(log_entry)


if __name__ == "__main__":
    main()
