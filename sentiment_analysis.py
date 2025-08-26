from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize VADER sentiment analyzer
sentiments = SentimentIntensityAnalyzer()


data["verified_reviews"] = data["verified_reviews"].fillna("").astype(str)

# Apply sentiment analysis safely
data["Positive"] = [sentiments.polarity_scores(i)["pos"] for i in data["verified_reviews"]]
data["Negative"] = [sentiments.polarity_scores(i)["neg"] for i in data["verified_reviews"]]
data["Neutral"]  = [sentiments.polarity_scores(i)["neu"] for i in data["verified_reviews"]]

# Display sample
print(data.head())

