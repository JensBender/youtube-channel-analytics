import gradio as gr
from transformers import pipeline
import pandas as pd

# Initialize sentiment analysis pipelines
roberta_pipeline = pipeline(
    task="sentiment-analysis", 
    model="cardiffnlp/twitter-roberta-base-sentiment-latest", 
    truncation=True, 
    max_length=512
)

distilbert_pipeline = pipeline(
    task="sentiment-analysis", 
    model="distilbert-base-uncased-finetuned-sst-2-english", 
    truncation=True, 
    max_length=512
)

# Function to perform sentiment analysis on multiple YouTube comments
def analyze_sentiment(data):
    # Convert comments from a list in the JSON input data to a Pandas DataFrame
    df = pd.DataFrame(data["comment_text"], columns=["comment_text"])

    # Store model choice from JSON input data
    model_choice = data["model_choice"].lower()

    # Perform sentiment analysis based on model choice
    if model_choice == "roberta":
        df["result"] = df["comment_text"].apply(lambda x: roberta_pipeline(x)[0])
    else:
        df["result"] = df["comment_text"].apply(lambda x: distilbert_pipeline(x)[0])
    
    # Extract sentiment and confidence into separate columns
    df[f"{model_choice}_sentiment"] = df["result"].apply(lambda x: x["label"].lower())
    df[f"{model_choice}_confidence"] = df["result"].apply(lambda x: round(x["score"], 3))

    # Output data in JSON format 
    output = {
        f"{model_choice}_sentiment": df[f"{model_choice}_sentiment"].tolist(),
        f"{model_choice}_confidence": df[f"{model_choice}_confidence"].tolist()
    }    

    return output

# Create Gradio interface
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.JSON(),
    outputs=gr.JSON(),
    title="Sentiment Analysis with RoBERTa and DistilBERT",
    description="Send a JSON object with a list of comments and the model choice via API request for sentiment analysis."
)

# Launch Gradio interface as a web application
iface.launch()
