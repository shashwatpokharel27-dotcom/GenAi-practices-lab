from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

from langchain_mistralai import ChatMistralAI

model=ChatMistralAI("mistral-small-2603")

data =PyPDFLoader(r"c:\Users\Admin HP\OneDrive\Desktop\Generative AI\RAG_projects\document_loader\GRU.pdf")

docs=data.load()

prompt=ChatPromptTemplate.from_messages(
    [ ( "system","you are ai that summarizes text" ),
      ("human","{text}")]
)

final_prompt = prompt.invoke({"text":docs[0].page_content})

res=model.invoke(final_prompt)

print(res)