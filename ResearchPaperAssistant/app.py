import streamlit as st

from create_database import DatabaseCreator
from main import ResearchPaperAssistant

st.set_page_config(page_title="Research Paper Assistant")

st.title("📚 Research Paper Assistant")

uploaded_files = st.file_uploader(
    "Upload Research Papers",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:

    if "assistant" not in st.session_state:

        with st.spinner("Creating Vector Database..."):

            creator = DatabaseCreator()

            vectorstore = creator.create_database(uploaded_files)

            st.session_state.assistant = ResearchPaperAssistant(
                vectorstore
            )

        st.success("Research papers indexed successfully!")

assistant = st.session_state.get("assistant")

if assistant:

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    question = st.chat_input("Ask about your research papers...")

    if question:

        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.spinner("Searching..."):

            answer, context = assistant.ask(question)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

        with st.expander("Retrieved Context"):
            st.write(context)