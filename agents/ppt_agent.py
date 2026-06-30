import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.0-flash")


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
    {text[:20000]}
    """

    response = model.generate_content(prompt)

    return response.text