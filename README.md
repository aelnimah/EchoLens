# EchoLens 🧠📊

> A lightweight AI-powered CLI tool for transforming raw feedback into actionable insights and interactive visualizations.

## 💡 What It Does

EchoLens helps you analyze open-ended user feedback with:
- ✅ Sentiment analysis
- ✅ Category classification
- ✅ AI-generated summary reports (via Google Gemini)
- ✅ Quadrant-style sentiment vs intensity graphs (Plotly)

Built for speed, simplicity, and flexibility — whether you're analyzing course reviews, survey results, or product feedback.

## 📂 How It Works

1. **Provide Project Info**  
   Enter name, description, and goal via CLI.

2. **Load Comments**  
   Point it to an Excel file (e.g. `sample_comments.xlsx`) with a `comment` column.

3. **Analyze**  
   Each comment is scored using TextBlob and categorized with keyword rules.

4. **Choose Your Output**
   - `1` Generate a smart AI summary with Gemini
   - `2` View a quadrant graph of sentiment vs intensity

## 📦 Dependencies

- `pandas`
- `textblob`
- `plotly`
- `google-generativeai`

Install them all with:

```bash
pip install -r requirements.txt
