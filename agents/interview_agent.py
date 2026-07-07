from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_interview_questions(text):

    prompt = f"""
    Analyze this research paper and generate:

    1. 5 Basic Questions
    2. 10 Technical Questions
    3. 5 Research-Oriented Questions
    4. 5 Viva Questions

    Return only questions.

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