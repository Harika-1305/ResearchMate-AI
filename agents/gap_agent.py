from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

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