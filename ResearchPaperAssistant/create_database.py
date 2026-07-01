import tempfile
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()


class DatabaseCreator:

    def __init__(self):

        self.embedding = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5"
        )

    def create_database(self, uploaded_files):

        documents = []

        for uploaded_file in uploaded_files:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            ) as tmp:

                tmp.write(uploaded_file.read())
                temp_path = tmp.name

            loader = PyPDFLoader(temp_path)
            documents.extend(loader.load())

            Path(temp_path).unlink()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(documents)

        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding
        )

        return vectorstore