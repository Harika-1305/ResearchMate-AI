import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.0-flash")


def generate_scorecard(text):

    prompt = f"""
    Act as a research paper reviewer.

    Evaluate the paper and score:

    Novelty (out of 10)
    Technical Complexity (out of 10)
    Dataset Quality (out of 10)
    Deployment Readiness (out of 10)
    Research Impact (out of 10)

    Also provide a short justification.

    Paper:
    {text[:20000]}
    """

    response = model.generate_content(prompt)

    return response.text