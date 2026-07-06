import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("📈 Product Analytics Dashboard")

df = pd.read_csv("datasets/product_usage.csv")

users = df["user_id"].nunique()

avg_session = round(df["session_duration"].mean(), 2)

premium_users = (df["premium"] == "Yes").sum()

songs_played = df["songs_played"].sum()

c1, c2, c3, c4 = st.columns(4)

c1.metric("👥 Users", f"{users:,}")

c2.metric("⏱ Avg Session", f"{avg_session} min")

c3.metric("💎 Premium Users", f"{premium_users:,}")

c4.metric("🎵 Songs Played", f"{songs_played:,}")
st.divider()

device = df["device"].value_counts()

fig = px.pie(
    values=device.values,
    names=device.index,
    title="📱 Device Distribution"
)

st.plotly_chart(fig, use_container_width=True)
country = df["country"].value_counts()

fig = px.bar(
    x=country.index,
    y=country.values,
    title="🌍 Users by Country",
    color=country.values,
    color_continuous_scale="Greens"
)

st.plotly_chart(fig, use_container_width=True)
feature = df["feature_used"].value_counts()

fig = px.bar(
    x=feature.index,
    y=feature.values,
    title="🎵 Feature Usage",
    color=feature.values,
    color_continuous_scale="Greens"
)

st.plotly_chart(fig, use_container_width=True)
premium = df["premium"].value_counts()

fig = px.pie(
    values=premium.values,
    names=premium.index,
    title="💎 Premium vs Free Users"
)

st.plotly_chart(fig, use_container_width=True)
fig = px.histogram(
    df,
    x="session_duration",
    nbins=25,
    title="⏱ Session Duration Distribution"
)

st.plotly_chart(fig, use_container_width=True)