import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

# Load API key
load_dotenv()

# Model
model = ChatMistralAI(model="mistral-small-2603")

st.set_page_config(
    page_title="Shashwat Love Guru",
    page_icon="❤️",
    layout="centered"
)

st.title("❤️ Shashwat Love Guru Chat Bot")

mode = st.selectbox(
    "Choose Personality",
    [
        "Sad Girlfriend",
        "Funny Girlfriend",
        "Angry Girlfriend",
        "Shashwat Love Guru"
    ]
)

# Initialize memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=f"You are a {mode} AI agent")
    ]

# Reset when mode changes
if "current_mode" not in st.session_state:
    st.session_state.current_mode = mode

if st.session_state.current_mode != mode:
    st.session_state.current_mode = mode
    st.session_state.messages = [
        SystemMessage(content=f"You are a {mode} AI agent")
    ]

# Display chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# User input
prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user"):
        st.write(prompt)

    try:
        response = model.invoke(
            st.session_state.messages
        )

        st.session_state.messages.append(
            AIMessage(content=response.content)
        )

        with st.chat_message("assistant"):
            st.write(response.content)

    except Exception as e:
        st.error(f"Error: {e}")