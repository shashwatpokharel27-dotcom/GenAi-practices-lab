from dotenv import load_dotenv

load_dotenv()


#Mistral
'''
from langchain.chat_models import init_chat_model

model = init_chat_model("mistral-small-2603",
    model_provider="mistralai")

response=model.invoke("hi how are you")

print(response.content)
'''
#GROQ
'''
from langchain.chat_models import init_chat_model

model=init_chat_model("meta-llama/llama-4-scout-17b-16e-instruct",
    model_provider="groq")
response=model.invoke("What is god")
print(response.content)
'''

#modal class for gemini , we can use init_chat_model also but for practice
'''
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

response=model.invoke("provide ai engineer roadmap")

print(response.content)
'''
#modal class for mistral ai

from langchain_mistralai import ChatMistralAI

model=ChatMistralAI(model="mistral-small-2603",temperature=1.0,max_tokens=20)# temperature jati badyo uti creativity(poem,song) badxa ra jati ghatyo uti logic(math, code)

res=model.invoke("write a poem on nepal ")
print(res.content)

'''
Provider	Typical Range
OpenAI	0–2
Groq (depends on model)	often 0–2
Gemini	usually 0–2
Mistral	0–1
'''

'''
For mistral ai tasks:

Coding → 0.0 to 0.2
General chat → 0.5 to 0.7
Stories/poems → 0.8 to 1.0
'''

'''
A token is not exactly a word.

Roughly:

1 token ≈ 3/4 of an English word
100 tokens ≈ 75 words
1000 tokens ≈ 750 words
'''