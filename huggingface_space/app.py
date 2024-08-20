import gradio as gr
from transformers import pipeline

# Initialize sentiment analysis pipelines
roberta_pipeline = pipeline(task="sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
distilbert_pipeline = pipeline(task="sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Function to perform sentiment analysis on a single YouTube comment
def analyze_sentiment(text, model_choice):
    if model_choice == "RoBERTa":
        result = roberta_pipeline(text)[0]
        label = result["label"].lower()
        score = result["score"]
    else:
        result = distilbert_pipeline(text)[0]   
        label = result["label"]
        score = result["score"]
    return f"Sentiment: {label}\nConfidence: {score:.3f}"


# Create Gradio interface
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=[
        gr.Textbox(lines=3, placeholder="Enter text here..."),
        gr.Dropdown(choices=["RoBERTa", "DistilBERT"], label="Select Model")
    ],
    outputs="text",
    title="Sentiment Analysis with RoBERTa and DistilBERT",
    description="Select a model and enter text to analyze its sentiment."
)

# Launch Gradio interface as a web application
iface.launch()
