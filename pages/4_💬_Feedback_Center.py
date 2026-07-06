import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("💬 Feedback Center")

df = pd.read_csv("datasets/reviews.csv")

df.columns = df.columns.str.strip().str.lower()

st.write(f"Total Reviews: {len(df):,}")
search = st.text_input(
    "🔍 Search Reviews"
)
rating_filter = st.selectbox(
    "⭐ Rating",
    ["All", 5, 4, 3, 2, 1]
)
results = df.copy()

if rating_filter != "All":
    results = results[results["rating"] == rating_filter]

if search:
    results = results[
        results["review"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

results = results.head(20)

for _, row in results.iterrows():

    st.container(border=True)

    st.markdown(f"### {'⭐' * int(row['rating'])}")

    st.write(row["review"])

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"👍 Likes: {row['total_thumbsup']}")

    with col2:
        st.write(f"📅 {row['time_submitted']}")

    st.divider()

sort_option = st.selectbox(
    "Sort By",
    [
        "Newest",
        "Most Helpful",
        "Highest Rating",
        "Lowest Rating"
    ]
)
if sort_option == "Newest":
    results = results.sort_values(
        "time_submitted",
        ascending=False
    )

elif sort_option == "Most Helpful":
    results = results.sort_values(
        "total_thumbsup",
        ascending=False
    )

elif sort_option == "Highest Rating":
    results = results.sort_values(
        "rating",
        ascending=False
    )

elif sort_option == "Lowest Rating":
    results = results.sort_values(
        "rating"
    )