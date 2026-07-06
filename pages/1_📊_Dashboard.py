import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------
# Page Config
# -------------------------------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="🎵",
    layout="wide"
)

st.title("🎵 Spotify Product Intelligence Dashboard")
st.caption("Executive overview of customer reviews and product health.")

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------

df = pd.read_csv("datasets/reviews.csv")

df.columns = df.columns.str.strip().str.lower()

df["time_submitted"] = pd.to_datetime(df["time_submitted"])

# -------------------------------------------------
# KPI Calculations
# -------------------------------------------------

total_reviews = len(df)

avg_rating = round(df["rating"].mean(), 2)

avg_helpful = round(df["total_thumbsup"].mean(), 2)

negative_reviews = len(df[df["rating"] <= 2])

positive_reviews = len(df[df["rating"] >= 4])

positive_percent = round((positive_reviews / total_reviews) * 100, 1)

negative_percent = round((negative_reviews / total_reviews) * 100, 1)

# -------------------------------------------------
# Product Health Score
# -------------------------------------------------

health_score = round(
    (
        (avg_rating / 5) * 50
        +
        positive_percent * 0.5
    ),
    1,
)

# -------------------------------------------------
# KPI Cards
# -------------------------------------------------

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "⭐ Average Rating",
    avg_rating
)

c2.metric(
    "💬 Total Reviews",
    f"{total_reviews:,}"
)

c3.metric(
    "👍 Avg Helpful Votes",
    avg_helpful
)

c4.metric(
    "🚨 Negative Reviews",
    f"{negative_reviews:,}"
)

c5.metric(
    "💚 Health Score",
    f"{health_score}/100"
)

st.divider()

# -------------------------------------------------
# Charts Row 1
# -------------------------------------------------

left, right = st.columns(2)

# Rating Distribution

rating_counts = (
    df["rating"]
    .value_counts()
    .sort_index()
)

fig = px.bar(
    x=rating_counts.index,
    y=rating_counts.values,
    labels={
        "x": "Rating",
        "y": "Reviews"
    },
    title="⭐ Rating Distribution",
    color=rating_counts.values,
    color_continuous_scale="Greens"
)

left.plotly_chart(
    fig,
    use_container_width=True
)

# Review Timeline

timeline = (
    df.groupby(df["time_submitted"].dt.date)
    .size()
    .reset_index(name="Reviews")
)

fig = px.line(
    timeline,
    x="time_submitted",
    y="Reviews",
    title="📅 Review Timeline",
    markers=True
)

right.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# -------------------------------------------------
# Charts Row 2
# -------------------------------------------------

left, right = st.columns(2)

# Positive vs Negative

sentiment = pd.DataFrame({

    "Sentiment": [
        "Positive",
        "Negative"
    ],

    "Reviews": [
        positive_reviews,
        negative_reviews
    ]

})

fig = px.pie(
    sentiment,
    values="Reviews",
    names="Sentiment",
    title="😊 Positive vs Negative Reviews",
    color_discrete_sequence=["#1DB954", "#E74C3C"]
)

left.plotly_chart(
    fig,
    use_container_width=True
)

# Top Helpful Reviews

right.subheader("🔥 Top Helpful Reviews")

top_reviews = (
    df.sort_values(
        by="total_thumbsup",
        ascending=False
    )[[
        "review",
        "rating",
        "total_thumbsup"
    ]]
    .head(10)
)

right.dataframe(
    top_reviews,
    use_container_width=True,
    hide_index=True
)

st.divider()

# -------------------------------------------------
# Quick Insights
# -------------------------------------------------

st.subheader("💡 Quick Product Insights")

insights = []

if avg_rating >= 4:
    insights.append(
        "⭐ Overall customer satisfaction is high."
    )
else:
    insights.append(
        "⚠️ Average rating is below 4. Focus on improving customer satisfaction."
    )

if positive_percent >= 70:
    insights.append(
        "😊 Majority of users leave positive reviews."
    )
else:
    insights.append(
        "🚨 Negative reviews require closer investigation."
    )

if avg_helpful >= 5:
    insights.append(
        "👍 Reviews receive strong community engagement."
    )

most_common_rating = rating_counts.idxmax()

insights.append(
    f"📊 Most common rating is {most_common_rating}★."
)

for item in insights:
    st.success(item)

st.divider()

# -------------------------------------------------
# Recent Reviews
# -------------------------------------------------

st.subheader("📝 Recent Reviews")

recent = (
    df.sort_values(
        by="time_submitted",
        ascending=False
    )[[
        "time_submitted",
        "review",
        "rating"
    ]]
    .head(10)
)

st.dataframe(
    recent,
    use_container_width=True,
    hide_index=True
)