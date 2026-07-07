from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

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
    {text[:5000]}
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