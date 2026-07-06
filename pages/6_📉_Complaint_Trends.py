import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Complaint Trends",
    layout="wide"
)

st.title("📉 Complaint Trends Dashboard")
st.markdown("Analyze user complaints and review patterns from Spotify reviews.")

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("datasets/reviews.csv")

df.columns = df.columns.str.strip().str.lower()

df["time_submitted"] = pd.to_datetime(df["time_submitted"])

# -----------------------------
# KPI Cards
# -----------------------------

negative_reviews = len(df[df["rating"] <= 2])

positive_reviews = len(df[df["rating"] >= 4])

average_rating = round(df["rating"].mean(), 2)

average_likes = round(df["total_thumbsup"].mean(), 2)

c1, c2, c3, c4 = st.columns(4)

c1.metric("🚨 Negative Reviews", f"{negative_reviews:,}")

c2.metric("😊 Positive Reviews", f"{positive_reviews:,}")

c3.metric("⭐ Average Rating", average_rating)

c4.metric("👍 Avg Helpful Votes", average_likes)

st.divider()

# -----------------------------
# Complaint Distribution
# -----------------------------

left, right = st.columns(2)

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
        "y": "Number of Reviews"
    },
    title="⭐ Rating Distribution",
    color=rating_counts.values,
    color_continuous_scale="Reds"
)

left.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Review Timeline
# -----------------------------

daily_reviews = (
    df.groupby(df["time_submitted"].dt.date)
    .size()
    .reset_index(name="reviews")
)

fig = px.line(
    daily_reviews,
    x="time_submitted",
    y="reviews",
    title="📅 Review Trend Over Time",
    markers=True
)

right.plotly_chart(fig, use_container_width=True)

st.divider()

# -----------------------------
# Helpful Negative Reviews
# -----------------------------

st.subheader("🔥 Most Helpful Negative Reviews")

negative = (
    df[df["rating"] <= 2]
    .sort_values(
        by="total_thumbsup",
        ascending=False
    )
    [["review", "rating", "total_thumbsup", "time_submitted"]]
    .head(10)
)

negative.columns = [
    "Review",
    "Rating",
    "Helpful Votes",
    "Date"
]

st.dataframe(
    negative,
    use_container_width=True
)

st.divider()

# -----------------------------
# Rating Pie Chart
# -----------------------------

left, right = st.columns(2)

fig = px.pie(
    values=rating_counts.values,
    names=rating_counts.index,
    title="⭐ Rating Share"
)

left.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Helpful Votes Distribution
# -----------------------------

fig = px.histogram(
    df,
    x="total_thumbsup",
    nbins=30,
    title="👍 Helpful Votes Distribution"
)

right.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# -----------------------------
# Monthly Complaint Trend
# -----------------------------

st.subheader("📈 Monthly Complaint Trend")

monthly = (
    df.groupby(df["time_submitted"].dt.to_period("M"))
    .size()
    .reset_index(name="reviews")
)

monthly["time_submitted"] = monthly["time_submitted"].astype(str)

fig = px.area(
    monthly,
    x="time_submitted",
    y="reviews",
    title="Monthly Review Volume"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# -----------------------------
# Summary Statistics
# -----------------------------

st.subheader("📋 Complaint Summary")

st.info(f"""
### Key Observations

- Total Reviews: **{len(df):,}**
- Negative Reviews: **{negative_reviews:,}**
- Positive Reviews: **{positive_reviews:,}**
- Average Rating: **{average_rating}/5**
- Average Helpful Votes: **{average_likes:.2f}**

### Recommendations

- Investigate recurring low-rated reviews.
- Focus on highly upvoted complaints as they likely affect more users.
- Monitor review spikes after app updates.
- Use feedback to prioritize bug fixes and feature improvements.
""")