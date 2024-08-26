import gradio as gr
from transformers import pipeline

# Initialize sentiment analysis pipelines
roberta_pipeline = pipeline(task="sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
distilbert_pipeline = pipeline(task="sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Function to perform sentiment analysis on multiple YouTube comments
def analyze_sentiment(texts, model_choice):
    results = []
    for text in texts:
        if model_choice == "RoBERTa":
            result = roberta_pipeline(text)[0]
        else:
            result = distilbert_pipeline(text)[0]  

        results.append({
            "sentiment": result["label"].lower(),
            "confidence": round(result["score"], 3)
        })
    return results

# Create Gradio interface
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=[
        gr.List(label="Enter Text(s)"),
        gr.Dropdown(choices=["RoBERTa", "DistilBERT"], label="Select Model")
    ],
    outputs=gr.JSON(),
    title="Sentiment Analysis with RoBERTa and DistilBERT",
    description="Select a model and enter text(s) to analyze sentiment. You can add multiple texts using the list input."
)

# Launch Gradio interface as a web application
iface.launch()
