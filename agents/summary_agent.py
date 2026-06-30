import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_summary(text):
    prompt = f"""
    Analyze this research paper.

    Return the response in this exact format:

    \n# Paper Title

    \n# Research Objective

    \n# Methodology

    \n# Dataset Used

    \n# Results

    \n# Key Contributions

    Paper Content:
    {text[:15000]}
    """

    response = model.generate_content(prompt)

    return response.text