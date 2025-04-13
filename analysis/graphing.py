import plotly.express as px
import pandas as pd
import webbrowser
from pathlib import Path

def show_quadrant(df):
    df["intensity"] = df["sentiment"].abs() * 10

    fig = px.scatter(
        df,
        x="sentiment",
        y="intensity",
        color="category",
        hover_data=["comment"],
        title="Quadrant View: Sentiment vs Intensity",
        labels={"sentiment": "Sentiment Polarity", "intensity": "Intensity Score"}
    )

    output_path = Path("output/graph_quadrant.html").resolve()
    fig.write_html(output_path)

    chrome_path = '"C:/Program Files/Google/Chrome/Application/chrome.exe" %s'
    webbrowser.get(chrome_path).open(f"file://{output_path}")

