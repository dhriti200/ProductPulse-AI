import streamlit as st
import pandas as pd
from ai.category import classify_review
from ai.sentiment import analyze_sentiment
#from ai.features import extract_feature
from ai.priority import detect_priority

st.title("🤖 AI Feedback Analyzer")

df = pd.read_csv("datasets/reviews.csv")

df.columns = df.columns.str.strip().str.lower()
review = st.selectbox(
    "Choose a Review",
    df["review"].head(100)
)
if st.button("Analyze"):

    result = analyze_sentiment(review)

    st.success("Analysis Complete")

    st.metric(
        "Sentiment",
        result["label"]
    )

    st.metric(
        "Confidence",
        f"{result['score']:.2%}"
    )

category = classify_review(review)
st.metric(
    "Category",
    category
)
#feature = extract_feature(review)

#st.metric(
 #   "Feature",
 #   feature
#)
priority = detect_priority(review)

st.metric(
    "Priority",
    priority
)