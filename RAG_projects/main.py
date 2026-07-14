from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

from langchain_mistralai import ChatMistralAI

model=ChatMistralAI("mistral-small-2603")

data =PyPDFLoader(r"c:\Users\Admin HP\OneDrive\Desktop\Generative AI\RAG_projects\document_loader\GRU.pdf")

docs=data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=1,
)

chunks=splitter.split_documents(docs)


prompt=ChatPromptTemplate.from_messages(
    [ ( "system","you are ai that summarizes text" ),
      ("human","{text}")]
)

final_prompt = prompt.invoke({"text":chunks.page_content})

res=model.invoke(final_prompt)

print(res)