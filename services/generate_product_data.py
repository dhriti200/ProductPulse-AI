print("Script started")
import pandas as pd
import random
from faker import Faker

fake = Faker()

FEATURES = [
    "Search",
    "Playlist",
    "AI DJ",
    "Lyrics",
    "Podcasts",
    "Offline Download",
    "Queue",
    "Discover Weekly",
    "Wrapped"
]

DEVICES = [
    "Android",
    "iOS",
    "Web",
    "Desktop"
]

COUNTRIES = [
    "India",
    "USA",
    "UK",
    "Canada",
    "Germany",
    "Australia"
]

rows = []

for user_id in range(1, 10001):

    rows.append({

        "user_id": user_id,

        "date": fake.date_between(
            start_date="-365d",
            end_date="today"
        ),

        "session_duration": random.randint(5, 180),

        "songs_played": random.randint(1, 80),

        "device": random.choice(DEVICES),

        "country": random.choice(COUNTRIES),

        "premium": random.choice(["Yes", "No"]),

        "feature_used": random.choice(FEATURES)

    })

df = pd.DataFrame(rows)

df.to_csv(
    "datasets/product_usage.csv",
    index=False
)

print("✅ product_usage.csv created!")