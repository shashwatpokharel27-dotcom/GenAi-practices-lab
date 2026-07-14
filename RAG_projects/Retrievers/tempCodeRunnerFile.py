from langchain_community.retrievers import ArxivRetriever
from rich import print
#create the retriever 
retriever=ArxivRetriever(
    load_max_docs=3,
    load_all_available_meta=True
)

docs=retriever.invoke("large language models")

print(docs)