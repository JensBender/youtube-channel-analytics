import gradio as gr
from transformers import pipeline

# Load the sentiment analysis pipeline using DistilBERT fine-tuned on SST-2
sentiment_pipeline = pipeline(task="sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


# Define function for sentiment analysis of a single YouTube comment
def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = result["label"]
    score = result["score"]
    return f"Sentiment: {label}\nConfidence: {score:.4f}"


# Create the Gradio interface
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=3, placeholder="Enter text here..."),
    outputs="text",
    title="Sentiment Analysis with DistilBERT",
    description="Enter some text to analyze its sentiment."
)

# Launch the app
iface.launch()