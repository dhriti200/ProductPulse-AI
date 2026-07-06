import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("🎵 Feature Usage Analytics")

df = pd.read_csv("datasets/product_usage.csv")

feature_counts = df["feature_used"].value_counts()

most_used = feature_counts.idxmax()

least_used = feature_counts.idxmin()

total_features = df["feature_used"].nunique()

top_usage = feature_counts.max()

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "🔥 Most Used",
    most_used
)

c2.metric(
    "📉 Least Used",
    least_used
)

c3.metric(
    "🎵 Total Features",
    total_features
)

c4.metric(
    "👥 Highest Usage",
    top_usage
)
fig = px.bar(
    feature_counts,
    x=feature_counts.index,
    y=feature_counts.values,
    color=feature_counts.values,
    title="Feature Usage Distribution",
    color_continuous_scale="Greens"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
premium_feature = (
    df.groupby(
        ["feature_used", "premium"]
    )
    .size()
    .reset_index(name="users")
)

fig = px.bar(
    premium_feature,
    x="feature_used",
    y="users",
    color="premium",
    barmode="group",
    title="Premium vs Free Feature Usage"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
country_feature = (
    df.groupby(
        ["country", "feature_used"]
    )
    .size()
    .reset_index(name="count")
)

fig = px.sunburst(
    country_feature,
    path=[
        "country",
        "feature_used"
    ],
    values="count",
    title="Country-wise Feature Usage"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.subheader("Top Features")

table = (
    feature_counts
    .reset_index()
)

table.columns = [
    "Feature",
    "Users"
]

st.dataframe(
    table,
    use_container_width=True
)
