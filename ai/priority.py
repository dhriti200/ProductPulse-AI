def detect_priority(review):

    review = review.lower()

    critical = [
        "crash",
        "payment",
        "login",
        "refund",
        "cannot"
    ]

    high = [
        "bug",
        "error",
        "slow",
        "issue"
    ]

    medium = [
        "feature",
        "wish",
        "improve"
    ]

    if any(word in review for word in critical):
        return "Critical"

    if any(word in review for word in high):
        return "High"

    if any(word in review for word in medium):
        return "Medium"

    return "Low"