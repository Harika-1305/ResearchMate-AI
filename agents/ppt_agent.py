from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_ppt(text):

    prompt = f"""
    Analyze the research paper and generate
    a professional PowerPoint presentation.

    Create:

    Slide 1: Title
    Slide 2: Introduction
    Slide 3: Problem Statement
    Slide 4: Objectives
    Slide 5: Methodology
    Slide 6: Dataset
    Slide 7: Results
    Slide 8: Research Gaps
    Slide 9: Future Scope
    Slide 10: Conclusion

    For each slide provide:
    - Slide Title
    - Bullet Points

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