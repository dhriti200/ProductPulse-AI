from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

labels = [
    "Bug",
    "Performance",
    "UI",
    "Feature Request",
    "Ads",
    "Premium",
    "Playback",
    "Playlist",
    "Offline Download",
    "Podcasts",
    "Lyrics",
    "Search"
]


def classify_review(review):

    result = classifier(
        review,
        labels
    )

    return result["labels"][0]