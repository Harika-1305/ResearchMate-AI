import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_research_gaps(text):

    prompt = f"""
    Analyze the following research paper and provide:

    1. Research Gaps
    2. Limitations of the Study
    3. Missing Experiments
    4. Future Research Directions
    5. Novel Ideas to Improve the Work

    Format the response using headings and bullet points.

    Research Paper:
    {text[:20000]}
    """

    response = model.generate_content(prompt)

    return response.text