from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import Optional

# ---------------------------
# Model
# ---------------------------

model = ChatMistralAI(model="mistral-small-2603")

# ---------------------------
# Schema
# ---------------------------

class StockNews(BaseModel):
    company: str
    stock_change_percent: Optional[float]
    movement: str
    reason: str
    sentiment: str
    sector: Optional[str]

# ---------------------------
# Parser
# ---------------------------

parser = PydanticOutputParser(
    pydantic_object=StockNews
)

# ---------------------------
# Prompt
# ---------------------------

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Extract stock market information from the given news paragraph.

{format_instructions}
"""
    ),
    (
        "human",
        "{paragraph}"
    )
])

# ---------------------------
# Streamlit UI
# ---------------------------

st.set_page_config(
    page_title="Nepali Share Market News Extractor",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Nepali Share Market News Extractor")

st.write(
    "Paste a Nepali stock market news paragraph and extract structured information."
)

paragraph = st.text_area(
    "Enter News Paragraph",
    height=250,
    placeholder="Paste stock market news here..."
)

if st.button("Extract Information"):

    if not paragraph.strip():
        st.warning("Please enter a news paragraph.")
    else:

        with st.spinner("Analyzing News..."):

            final_prompt = prompt.invoke(
                {
                    "paragraph": paragraph,
                    "format_instructions": parser.get_format_instructions()
                }
            )

            response = model.invoke(final_prompt)

            stock_data = parser.parse(response.content)

        st.success("Extraction Completed!")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Company", stock_data.company)
            st.metric("Movement", stock_data.movement)
            st.metric("Sentiment", stock_data.sentiment)

        with col2:
            st.metric(
                "Stock Change %",
                stock_data.stock_change_percent
                if stock_data.stock_change_percent is not None
                else "N/A"
            )
            st.metric(
                "Sector",
                stock_data.sector
                if stock_data.sector
                else "N/A"
            )

        st.subheader("Reason")
        st.write(stock_data.reason)

        st.subheader("Structured Output")

        st.json(stock_data.model_dump())