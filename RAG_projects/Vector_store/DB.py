from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_core .documents import Document


load_dotenv()

docs = [
    Document(page_content="Python is widely used in Artificial Intelligence.", metadata={"source": "AI_book"}),
    Document(page_content="Pandas is used for data analysis in Python.", metadata={"source": "DataScience_book"}),
    Document(page_content="Neural networks are used in deep learning.", metadata={"source": "DL_book"}),
]

embedding_model=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="Chroma_db"
)

result =vector_store.similarity_search("What is used for datanalysis")
print("qns:What is used for datanalysis")

for i in result:
    print(i.page_content)
    print(i.metadata)

print("qns:What is neural networks")    

result2=vector_store.similarity_search("What is neural networks")

for r in result2:
    print(r.page_content)
    print(r.metadata)


ret=vector_store.as_retriever()

print("retriever:Explain deep learning")

docs=ret.invoke("Explain deep learning")
for i in docs:
    print(i.page_content)
