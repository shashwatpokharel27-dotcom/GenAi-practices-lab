from langchain_community.document_loaders import WebBaseLoader
url="https://en.wikipedia.org/wiki/The_Emperor_of_All_Maladies"

data=WebBaseLoader(url)
docs=data.load()

print(data)
print("===========================================")
print(docs)
print("===========================================")
print(docs[0].page_content)
