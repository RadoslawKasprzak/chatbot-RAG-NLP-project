import streamlit as st
import html

st.set_page_config(page_title="Pomocnik studenta", layout="centered")


if "messages" not in st.session_state:
    st.session_state["messages"] = []



st.markdown(
    """
    <style>
    .title {
        font-size: 20px;
        font-weight: 800;

    }
    /* Scrollable chat area styling */
    .chat-display {
        height: 45vh; /* Limit the height of the chat container */
        overflow-y: scroll; /* Add vertical scroll */
        padding: 10px;
        margin-bottom: 5px;
        background-color: #f8f8f8;
        border: 1px solid #ddd;
        border-radius: 10px;
        display: flex;
        flex-direction: column-reverse;
        border: 3px solid purple;
    }
    .chat-container {
        border: 2px solid purple;
        border-radius: 10px;
        padding: 2px;
        margin-bottom: 10px;
        background-color: #f9f9f9;
        width: 80%; /* Adjust width for narrower chat */
        margin-left: auto;  /* Center the chat box */
        margin-right: auto; /* Center the chat box */
    }
    .user-message {
        text-align: left;
        color: black;
        width: 50%;
        font-weight: bold;
        transform: translate(50%, 0%);
    }
    .bot-message {
        text-align: left;
        color: gray;
        width: 50%;
         transform: translate(-50%, 0%);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">Pomocnik Studenta</div>', unsafe_allow_html=True)

html_messages_string = ''

for message in st.session_state["messages"]:


    if message["role"] == "user":
        user_message = html.escape(message["content"])
        html_messages_string =  f'<div class="chat-container user-message">User: {user_message}</div>' + html_messages_string
    else:
        bot_message = html.escape(message["content"])
        html_messages_string =   f'<div class="chat-container bot-message">Bot: {bot_message}</div>'+ html_messages_string
html_messages_string = '<div class="chat-display">' + html_messages_string + '</div>'


st.markdown(html_messages_string, unsafe_allow_html=True)
# Function to send a new message
def send_message():
    user_input = st.session_state["user_input"]
    if user_input:
        # Store user message
        st.session_state["messages"].append({"role": "user", "content": user_input})

        # Simulate bot response (replace with actual bot logic if available)
        bot_response = f"Echo: {user_input}"  # This is where you could add bot logic
        st.session_state["messages"].append({"role": "bot", "content": bot_response})

        # Clear the input box
        st.session_state["user_input"] = ""


st.text_input("Twoja wiadomość:", key="user_input", on_change=send_message, placeholder="Type your message here...", )