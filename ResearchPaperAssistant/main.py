from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

class ResearchPaperAssistant:

    def __init__(self, vectorstore):

        self.retriever = vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 4,
                "fetch_k": 10,
                "lambda_mult": 0.5
            }
        )

        self.llm = ChatMistralAI(
            model="mistral-small-2603"
        )

        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
You are an AI Research Assistant.

Answer ONLY from the uploaded papers.

If the answer is unavailable, say:

"I could not find this information in the uploaded papers."
"""
                ),
                (
                    "human",
                    """
Context:
{context}

Question:
{question}
"""
                )
            ]
        )

    def ask(self, question):

        docs = self.retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        final_prompt = self.prompt.invoke(
            {
                "context": context,
                "question": question
            }
        )

        response = self.llm.invoke(final_prompt)

        return response.content, context