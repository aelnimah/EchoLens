# analysis/analyzer.py

from textblob import TextBlob

# Basic keyword mapping
CATEGORY_KEYWORDS = {
    "project": "Group Project",
    "lecture": "Lectures",
    "slides": "Lectures",
    "ta": "TA Support",
    "feedback": "Feedback",
    "sprint": "Agile Workflow",
    "midterm": "Assessments",
    "example": "Lectures",
    "design": "Course Content",
    "overwhelm": "Workload",
}

def analyze_comment(text):
    # Sentiment score
    sentiment = TextBlob(text).sentiment.polarity  # from -1 (neg) to 1 (pos)

    # Category detection based on keywords
    text_lower = text.lower()
    category = "General"
    for keyword, cat in CATEGORY_KEYWORDS.items():
        if keyword in text_lower:
            category = cat
            break

    return {
        "comment": text,
        "sentiment": round(sentiment, 3),
        "category": category
    }