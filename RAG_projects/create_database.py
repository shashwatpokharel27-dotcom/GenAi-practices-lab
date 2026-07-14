from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

embedding_model=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
data=PyPDFLoader(r"c:\Users\Admin HP\OneDrive\Desktop\Generative AI\RAG_projects\document_loader\deeplearning.pdf")

docs=data.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks=splitter.split_documents(docs)

vectorstore=Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="dp_chroma_db")