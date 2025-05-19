# llm_analyzer.py

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_with_llm(input_text):
    model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-01-21")

    prompt = (
        "You're an AI security analyst. Analyze the following web page content for phishing risk.\n"
        "Consider aspects from HTML, extracted images (OCR), and DOM structure.\n"
        "Rate the likelihood of phishing using the following format only:\n\n"
        "Score: <0–10>   # 0 = Safe, 10 = Definite Phishing\n"
        "Explanation: <brief explanation of why this score was given>\n\n"
        f"{input_text}"
    )

    response = model.generate_content(prompt)
    result_text = response.text.strip()

    # Parse response
    score = 0
    explanation = result_text

    for line in result_text.splitlines():
        if "Score:" in line:
            try:
                score = int(line.split(":", 1)[1].strip())
            except ValueError:
                score = -1
        elif "Explanation:" in line:
            explanation = line.split(":", 1)[1].strip()

    if score >= 7:
        verdict = "Phishing"
    elif score >= 4:
        verdict = "Suspicious"
    else:
        verdict = "Safe"

    return {
        "phishing_score": score,
        "verdict": verdict,
        "explanation": explanation
    }