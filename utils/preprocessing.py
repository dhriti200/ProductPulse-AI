import pandas as pd


def load_reviews():
    df = pd.read_csv("datasets/reviews.csv")
    return df


def clean_reviews(df):
    # Remove duplicate reviews
    df = df.drop_duplicates()

    # Remove rows with missing values
    df = df.dropna()

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()

    return df