import gradio as gr
from transformers import pipeline
import pandas as pd

# Initialize sentiment analysis pipeline
roberta_pipeline = pipeline(
    task="sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    truncation=True,
    max_length=512
)

# Function to perform sentiment analysis on multiple YouTube comments
def analyze_sentiment(data):
    # Convert comments from a list in the JSON input data to a Pandas DataFrame
    df = pd.DataFrame(data["comment_text"], columns=["comment_text"])
    
    # Perform sentiment analysis
    df["result"] = df["comment_text"].apply(lambda x: roberta_pipeline(x)[0])
   
    # Extract sentiment and confidence into separate columns
    df["roberta_sentiment"] = df["result"].apply(lambda x: x["label"].lower())
    df["roberta_confidence"] = df["result"].apply(lambda x: round(x["score"], 3))
    
    # Output data in JSON format
    output = {
        "roberta_sentiment": df["roberta_sentiment"].tolist(),
        "roberta_confidence": df["roberta_confidence"].tolist()
    }    
    return output

# Create Gradio interface
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.JSON(),
    outputs=gr.JSON(),
    title="Sentiment Analysis with RoBERTa",
    description="Send a JSON object with a list of comments via API request for sentiment analysis."
)

# Launch Gradio interface as a web application
iface.launch()
