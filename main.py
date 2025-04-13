# main.py

import os
import pandas as pd
from datetime import datetime
from analysis.analyzer import analyze_comment

def get_project_info():
    print("\nEnter Project Info")
    name = input("Project Name: ")
    description = input("Description: ")
    goal = input("Project Goal: ")

    return {
        "name": name,
        "description": description,
        "goal": goal,
        "created_at": datetime.now().isoformat()
    }


def load_comments(filepath):
    print("\nLoading comments from:", filepath)
    df = pd.read_excel(filepath)
    if "comment" not in df.columns:
        raise ValueError("Missing comment column.")
    return df

if __name__ == "__main__":
    print("=== CLI ===")
    project = get_project_info()
    project_context = {
        "name": project["name"],
        "description": project["description"],
        "goal": project["goal"]
    }
    
    path = "data/sample_comments.xlsx"
    try:
        comments_df = load_comments(path)
        print(f"Loaded {len(comments_df)} comments.")
    except Exception as e:
        print("Error:", e)

    print("\nAnalyzing comments...")
    results = []

    for comment in comments_df["comment"]:
        analysis = analyze_comment(comment)
        results.append(analysis)

    # Save to CSV
    output_df = pd.DataFrame(results)
    os.makedirs("output", exist_ok=True)
    output_path = "output/analyzed_comments.csv"
    output_df.to_csv(output_path, index=False)

    print(f"Analysis complete. Output saved to: {output_path}")

    while True:
        print("\n Options:")
        print("1) Summary Analysis")
        print("2) Generate Quadrant Graph (Sentiment vs Intensity)")
        print("3) Exit")
        choice = input("Option: ")

        if choice == "1":
            from analysis.summary import generate_summary
            generate_summary(project, output_df)
        
        elif choice == "2":
            from analysis.graphing import show_quadrant
            show_quadrant(output_df)

        elif choice == "3":
            print("Exiting.")
            break

        else:
            print("Invalid choice.")

# Project Name: Carleton Course Feedback – COMP 3004
# Description: Gathering feedback from CS students to improve the course
# Goal: Understand sentiment and suggestions
