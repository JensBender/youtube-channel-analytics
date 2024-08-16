import gradio as gr
from transformers import pipeline

# Initialize sentiment analysis pipeline using the DistilBERT model fine-tuned on SST-2
sentiment_pipeline = pipeline(task="sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


# Function to perform sentiment analysis on a single YouTube comment
def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = result["label"]
    score = result["score"]
    return f"Sentiment: {label}\nConfidence: {score:.3f}"


# Create Gradio interface
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=3, placeholder="Enter text here..."),
    outputs="text",
    title="Sentiment Analysis with DistilBERT",
    description="Enter a text to analyze its sentiment."
)

# Launch Gradio interface as a web application
iface.launch()
