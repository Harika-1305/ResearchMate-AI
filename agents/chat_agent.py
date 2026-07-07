from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def chat_with_paper(text, question):

    prompt = f"""
    You are an intelligent research assistant.

    Answer the user's question only using
    the information available in the paper.

    Research Paper:
    {text[:5000]}

    User Question:
    {question}
    """

    try:

        response = client.chat.completions.create(
            model="openrouter/free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"API Error: {str(e)}"