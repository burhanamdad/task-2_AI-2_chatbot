from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def ask_llm(question, context):

    prompt = f"""
Answer ONLY from provided context.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(

        model="deepseek/deepseek-chat",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content