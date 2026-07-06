from utils.preprocessing import load_reviews, clean_reviews

df = load_reviews()
df = clean_reviews(df)

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())