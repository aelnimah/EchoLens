# llm/summary.py

import google.generativeai as genai
import os

# Load Gemini API key
genai.configure(api_key="AIzaSyBKuw6PKNI8iDuP9U8u0z2p5CsnTIE-41U")

def generate_summary(project, df):
    print("\nSending project data to Gemini...")

    comments_text = "\n".join(
        f"- {row['comment']} (Category: {row['category']}, Sentiment: {row['sentiment']})"
        for _, row in df.iterrows()
    )

    prompt = (
        f"Project Name: {project['name']}\n"
        f"Description: {project['description']}\n"
        f"Goal: {project['goal']}\n\n"
        f"Analyzed Comments:\n{comments_text}\n\n"
        "Please generate a professional project summary including:\n"
        "- Key themes and insights\n"
        "- Sentiment trends\n"
        "- Suggested improvements\n"
        "- Any critical observations or gaps"
    )

    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        summary = response.text

        print("\nSummary:\n")
        print(summary)

        os.makedirs("output", exist_ok=True)
        with open("output/project_summary.txt", "w", encoding="utf-8") as f:
            f.write(summary)
        print("\nSaved to: output/project_summary.txt")

    except Exception as e:
        print("Gemini summary failed:", e)
