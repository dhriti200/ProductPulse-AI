from transformers import pipeline

sentiment_pipeline = pipeline(
    "sentiment-analysis"
)

def analyze_sentiment(review):

    result = sentiment_pipeline(review)[0]

    return result