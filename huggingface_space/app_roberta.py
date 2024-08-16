import gradio as gr
from transformers import pipeline

# Initialize sentiment analysis pipeline using the RoBERTa model fine-tuned on Twitter data
sentiment_pipeline = pipeline(task="sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

# Define mapping from model output labels to human-readable labels
label_mapping = {
    "LABEL_0": "Negative",
    "LABEL_1": "Neutral",
    "LABEL_2": "Positive"
}


# Function to perform sentiment analysis on a single YouTube comment
def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = label_mapping[result["label"]]  
    score = result["score"]
    return f"Sentiment: {label}\nConfidence: {score:.3f}"


# Create Gradio interface
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=3, placeholder="Enter text here..."),
    outputs="text",
    title="Sentiment Analysis with RoBERTa",
    description="Enter a text to analyze its sentiment."
)

# Launch Gradio interface as a web application
iface.launch()
