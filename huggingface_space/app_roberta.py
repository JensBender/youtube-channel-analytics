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

# Function to perform sentiment analysis on single YouTube comment
def analyze_single_sentiment(comment):
    try:
        result = roberta_pipeline(comment)[0]
        # Check if result is a dictionary with 'label' and 'score' keys
        if isinstance(result, dict) and "label" in result and "score" in result:
            return result
        else:
            # Return a default dictionary if the result doesn't match the expected format
            return {"label": "unknown", "score": 0.0}
    except Exception as e:
        # Log the error and return a default dictionary
        print(f"Error analyzing comment: '{comment}', Error: {str(e)}")
        return {"label": "error", "score": 0.0}
    
# Function to perform sentiment analysis on multiple YouTube comments
def analyze_sentiment(data):
    # Check correct input data format 
    if "comment_text" not in data or not isinstance(data["comment_text"], list):
        raise ValueError("Input must be a dictionary with a 'comment_text' key containing a list of comments")
    
    # Convert comments from a list in the JSON input data to a Pandas DataFrame
    df = pd.DataFrame(data["comment_text"], columns=["comment_text"])

    # Apply sentiment analysis to all comments   
    df["result"] = df["comment_text"].apply(analyze_single_sentiment)
   
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
