from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

model=ChatMistralAI(model="mistral-small-2603")

#short term memory
'''
messages=[]

print("welcome to program and for exit type 0 ")

#loop to break 
while True:
  
    prompt= input("You:")

    messages.append(prompt)

    if prompt=="0":
        break
    
    res=model.invoke(messages)

    messages.append(res.content)
    print("Bot:",res.content)

print(messages)

'''

#memory using langchain 

from langchain_core.messages import AIMessage,SystemMessage,HumanMessage

print('the mode you need\n')
print("choose:-------------------- \n 1 for Sad Girlfriend \n 2 for Funny Girlfriend \n 3 for Angry Girlfriend \n 4 for Shashwat love guru")
print("------------------------------------------------------------------------------------")
choose=int (input("tell your response:"))


if choose==1:
    mode='Sad Girlfriend'
elif choose==2:
    mode='Funny Girlfriend'

elif choose==3:
    mode='Angry Girlfriend'

elif choose==4:
    mode='Love guru '

messages=[SystemMessage(content=f'you are {mode} ai agent')]
print("------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------")
print("welcome to Shashwat Love guru Chat Bot where you can")

#loop to break 
while True:
  
    prompt= input("You:")

    messages.append(HumanMessage(content=prompt))

    if prompt=="0":
        break
    
    res=model.invoke(messages)

    messages.append(AIMessage(content=res.content))
    print("Bot:",res.content)

print(messages)
