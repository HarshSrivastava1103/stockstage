import streamlit as st

st.title('Welcome to the Stock Analysis Chatbot Assistant!')

user_name = st.text_input("What's your name?")

if user_name:
    st.write(f"Hello, {user_name}! How can I assist you today?")

# Function for stock analysis can be defined here, if necessary

if "messages" not in st.session_state:
    st.session_state.messages = []

if user_input := st.text_input("Send a message"):
    st.session_state.messages.append({'role': 'user', 'content': f'{user_input}'})

    with st.empty():
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.write(f'User: {message["content"]}')
            elif message["role"] == "assistant":
                st.write(f'Assistant: {message["content"]}')
                if message["content"] == 'stock.png':
                    st.image('stock.png')
