from langchain_community.document_loaders import PyPDFLoader

data =PyPDFLoader(r"c:\Users\Admin HP\OneDrive\Desktop\Generative AI\RAG_projects\document_loader\GRU.pdf")

docs = data.load()

print(docs)
print("===========================================")
print(len(docs))
print("===========================================")
print(docs[0])
print("===========================================")

