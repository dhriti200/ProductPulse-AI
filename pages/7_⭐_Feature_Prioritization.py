import streamlit as st
import pandas as pd
import plotly.express as px
import random

st.set_page_config(
    page_title="Feature Prioritization",
    layout="wide"
)

st.title("⭐ Feature Prioritization (RICE Framework)")

st.markdown(
    "Prioritize Spotify features based on Reach, Impact, Confidence and Effort."
)

# ------------------------
# Load Dataset
# ------------------------

df = pd.read_csv("datasets/product_usage.csv")

feature_usage = (
    df["feature_used"]
    .value_counts()
    .reset_index()
)

feature_usage.columns = [
    "Feature",
    "Reach"
]

# ------------------------
# Generate Product Metrics
# ------------------------

random.seed(42)

feature_usage["Impact"] = [
    random.randint(1, 5)
    for _ in range(len(feature_usage))
]

feature_usage["Confidence"] = [
    random.randint(60, 100)
    for _ in range(len(feature_usage))
]

feature_usage["Effort"] = [
    random.randint(1, 10)
    for _ in range(len(feature_usage))
]

feature_usage["RICE Score"] = (
    feature_usage["Reach"]
    * feature_usage["Impact"]
    * feature_usage["Confidence"]
) / feature_usage["Effort"]

feature_usage = feature_usage.sort_values(
    "RICE Score",
    ascending=False
)

# ------------------------
# KPI Cards
# ------------------------

c1, c2, c3 = st.columns(3)

c1.metric(
    "🥇 Highest Priority",
    feature_usage.iloc[0]["Feature"]
)

c2.metric(
    "📊 Avg RICE Score",
    round(feature_usage["RICE Score"].mean(),1)
)

c3.metric(
    "🎵 Features",
    len(feature_usage)
)

st.divider()

# ------------------------
# RICE Ranking Table
# ------------------------

st.subheader("🏆 Feature Ranking")

st.dataframe(
    feature_usage,
    use_container_width=True
)

st.divider()

# ------------------------
# Bar Chart
# ------------------------

fig = px.bar(
    feature_usage,
    x="Feature",
    y="RICE Score",
    color="RICE Score",
    color_continuous_scale="Greens",
    title="Feature Priority Ranking"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ------------------------
# Bubble Chart
# ------------------------

fig = px.scatter(
    feature_usage,
    x="Reach",
    y="Impact",
    size="RICE Score",
    color="RICE Score",
    hover_name="Feature",
    title="Reach vs Impact"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ------------------------
# Recommendations
# ------------------------

st.subheader("🚀 Product Recommendations")

top3 = feature_usage.head(3)

for _, row in top3.iterrows():

    st.success(
        f"Prioritize **{row['Feature']}** "
        f"(RICE Score: {row['RICE Score']:.1f})"
    )

st.info("""
### How RICE Works

- Reach → Number of users affected
- Impact → Expected business impact
- Confidence → Confidence in estimates
- Effort → Engineering effort required

Higher RICE score = Higher Priority
""")