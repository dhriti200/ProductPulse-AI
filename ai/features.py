FEATURES = [
    "AI DJ",
    "Offline Download",
    "Playlist",
    "Search",
    "Podcasts",
    "Premium",
    "Lyrics",
    "Playback",
    "Queue",
    "Downloads"
]


def extract_feature(review):

    review = review.lower()

    for feature in FEATURES:

        if feature.lower() in review:

            return feature

    return "General"