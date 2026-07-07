from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

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
    {text[:3000]}
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