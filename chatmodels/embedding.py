from langchain_huggingface import HuggingFaceEmbeddings

embeddings=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

#For single text embedding
'''
vector=embeddings.embed_query("you are going to learn genai")

print(vector)
'''

#For many texts and documents

'''
texts=[
    'hi you are a good boy',
    'no you are a bad boy',
    'you are simple not good nor bad boy'
]
vector=embeddings.embed_documents(texts)
print(vector)

'''

'''
Convert text → vector

The sentence:

you are going to learn genai

gets converted into a list of numbers like:

[-0.0138, -0.0141, 0.0029, ...]
    ↓
[384-dimensional vector]

These numbers are the embedding.
'''

'''
Example:

Document 1: "LangChain is a framework for LLMs"
Document 2: "Nepal is a country in South Asia"

Query: "What is LangChain?"

Embedding compares vectors and finds:
→ Document 1 is most similar
'''