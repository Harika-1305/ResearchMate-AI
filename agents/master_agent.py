import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.0-flash"
)


def generate_master_analysis(text):

    prompt = f"""
    Analyze this research paper.

    Return EXACTLY in this format:

    ## METADATA
    Title:
    Authors:
    Year:
    DOI:
    Keywords:

    ## SUMMARY
    ...

    ## RESEARCH_GAPS
    ...

    ## QUESTIONS
    ...

    ## PPT
    ...

    ## SCORECARD
    ...

    Paper:
    {text[:20000]}
    """

    response = model.generate_content(prompt)

    return response.text