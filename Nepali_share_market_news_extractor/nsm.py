from langchain_mistralai import ChatMistralAI

from langchain_core.prompts import ChatPromptTemplate


'''
PromptTemplate → single text prompt
ChatPromptTemplate → chat models (ChatMistralAI, ChatOpenAI)
'''

'''
PromptTemplate

Creates a plain text prompt:

prompt = PromptTemplate.from_template(
    "Say {foo}"
)
and
ChatPromptTemplate

Creates structured chat messages:

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("human", "{question}")
])
'''

from dotenv import load_dotenv

load_dotenv()


model=ChatMistralAI(model="mistral-small-2603")


prompt = ChatPromptTemplate.from_messages(
[
    ( "system",
        """
You are an expert financial information extraction system.

Your task is to analyze a stock market news paragraph and extract structured information.

Rules:
- Extract only information explicitly stated or strongly implied in the text.
- Do not hallucinate or invent facts.
- If a field is not available, return null.
- Determine sentiment as positive, negative, or neutral.
- Identify the sector when possible.
- Return the output strictly according to the format instructions.
    """),
    (
        "human",
        """
        News Paragraph:

        {paragraph}
    
        """
    )

]
)

para=input("Enter Share Market News Paragraph:\n\n")

final_prompt = prompt.invoke({"paragraph": para})

res=model.invoke(final_prompt)

print(res)

