import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.0-flash")


def chat_with_paper(text, question):

    prompt = f"""
    You are an intelligent research assistant.

    Answer the user's question only using
    the information available in the paper.

    Research Paper:
    {text[:25000]}

    User Question:
    {question}
    """

    response = model.generate_content(prompt)

    return response.text