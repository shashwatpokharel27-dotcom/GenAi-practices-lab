from langchain_community.document_loaders import TextLoader

loader = TextLoader(r"c:\Users\Admin HP\OneDrive\Desktop\Generative AI\RAG_projects\document_loader\notes.txt", encoding="utf-8")
'''
encoding="utf-8" tells Python: "This file was saved using UTF-8, so decode it using UTF-8."
UTF-8 supports almost every language in the world:
'''

#here loader contain the content in object forn
docs=loader.load()

#loader.load() is calling the function that returns a docs(list of Document objects).

print(docs)
print(docs[0].page_content)
#docs[0] is a Document object.

'''
docs[0].page_content   # ✅ first document
docs[1].page_content   # ✅ second document (if exists)
docs.page_content      # ❌ list has no attribute 'page_content'
'''