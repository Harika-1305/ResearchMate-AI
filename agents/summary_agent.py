import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_summary(text):

    prompt = f"""
    Analyze this research paper and provide:

    1. Paper Title
    2. Research Objective
    3. Methodology
    4. Dataset Used
    5. Results
    6. Key Contributions

    Paper Content:
    {text[:15000]}
    """

    response = model.generate_content(prompt)

    return response.text