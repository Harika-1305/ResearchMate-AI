import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_interview_questions(text):

    prompt = f"""
    Analyze this research paper and generate:

    1. 5 Basic Questions
    2. 10 Technical Questions
    3. 5 Research-Oriented Questions
    4. 5 Viva Questions

    Return only questions.

    Paper:
    {text[:20000]}
    """

    response = model.generate_content(prompt)

    return response.text