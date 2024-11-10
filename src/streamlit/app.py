import streamlit as st

st.set_page_config(page_title="Pomocnik studenta", layout="wide")


if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.title("Pomocnik studenta")


for message in st.session_state["messages"]:
    if message["role"] == "user":
        st.write(f"**User**: {message['content']}")
    else:
        st.write(f"**Bot**: {message['content']}")

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

# Input box and send button
st.text_input("You:", key="user_input", on_change=send_message)