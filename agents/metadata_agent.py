import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.0-flash")


def extract_metadata(text):

    prompt = f"""
    Extract the following information from this research paper.

    Return ONLY:

    Title:
    Authors:
    Publication Year:
    DOI:
    Keywords:

    Paper:
    {text[:15000]}
    """

    response = model.generate_content(prompt)

    return response.text