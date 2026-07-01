from langchain_mistralai import ChatMistralAI

from langchain_core.prompts import ChatPromptTemplate

from pydantic import BaseModel

from langchain_core.output_parsers import PydanticOutputParser

from typing import Optional


from dotenv import load_dotenv

load_dotenv()


model=ChatMistralAI(model="mistral-small-2603")

#schema
class StockNews(BaseModel):
    company: str
    stock_change_percent: Optional[float]
    movement: str
    reason: str
    sentiment: str
    sector: Optional[str]

    #telling Python:"Every stock news output must have exactly these fields." This is like a blueprint.

#parser

parser=PydanticOutputParser(pydantic_object=StockNews)

#Give the blueprint to the parser.Now the parser learns:
'''
Expected format:
{
    "company": "...",
    "sentiment": "..."
}

'''




prompt=ChatPromptTemplate.from_messages([
    ("system",
     """
Extract stock market information from the given news paragraph.
{format_instructions}
"""),

('human',"{paragraph}"),

])

para=input("Enter Share Market News Paragraph:\n\n")

final_prompt = prompt.invoke({"paragraph": para,
                              "format_instructions":parser.get_format_instructions()})

'''
parser.get_format_instructions():

It generates instructions for the LLM.

Something similar to:

Return a JSON object with:

{
  "company": string,
  "sentiment": string
}
'''

res=model.invoke(final_prompt)

stock_data=parser.parse(res.content)
'''
This converts:

{
  "company": "NABIL Bank",
  "sentiment": "positive"
}

into a real Python object:

StockNews(
    company="NABIL Bank",
    sentiment="positive"
)

Now you can do:

print(stock_data.company)
'''


print(stock_data)

