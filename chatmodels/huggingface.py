from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()  

llm = HuggingFaceEndpoint(
    repo_id="MiniMaxAI/MiniMax-M3",
)

model=ChatHuggingFace(llm=llm)
response = model.invoke("Who are you?")

print(response.content)