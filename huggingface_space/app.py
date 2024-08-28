import gradio as gr
from transformers import pipeline

# Initialize sentiment analysis pipelines
roberta_pipeline = pipeline(task="sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
distilbert_pipeline = pipeline(task="sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Function to perform sentiment analysis on multiple YouTube comments
def analyze_sentiment(df, model_choice):
    if model_choice == "RoBERTa":
        df["result"] = df["comment"].apply(lambda x: roberta_pipeline(x)[0])
    else:
        df["result"] = df["comment"].apply(lambda x: distilbert_pipeline(x)[0])
    
    df[f"{model_choice.lower()}_sentiment"] = df["result"].apply(lambda x: x["label"].lower())
    df[f"{model_choice.lower()}_confidence"] = df["result"].apply(lambda x: round(x["score"], 3))
    return df

# Create Gradio interface
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=[
        gr.Dataframe(type="pandas", headers=["comment"]),
        gr.Dropdown(choices=["RoBERTa", "DistilBERT"], label="Select Model")
    ],
    outputs=gr.Dataframe(),
    title="Sentiment Analysis with RoBERTa and DistilBERT",
    description="Select a model and enter text(s) to analyze sentiment. You can add multiple texts using the dataframe input."
)

# Launch Gradio interface as a web application
iface.launch()
