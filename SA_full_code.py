# sentiment_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# -------------------------------------------------------------------
# Ensure VADER lexicon is available (downloads only if missing)
# -------------------------------------------------------------------
try:
    nltk.data.find("sentiment/vader_lexicon")
except LookupError:
    nltk.download("vader_lexicon")

# -------------------------------------------------------------------
# Load Dataset
# -------------------------------------------------------------------
data = pd.read_csv(
    "https://raw.githubusercontent.com/amankharwal/Website-data/master/amazon_alexa.tsv",
    delimiter="\t",
)
print("First 5 rows:\n", data.head())

# -------------------------------------------------------------------
# Dataset Info
# -------------------------------------------------------------------
print("\nDataset Summary:\n", data.describe())
print("\nMissing values:\n", data.isnull().sum())
print("\nColumns:\n", data.columns)

# -------------------------------------------------------------------
# Rating Breakdown (Donut Pie)
# -------------------------------------------------------------------
ratings = data["rating"].value_counts()
numbers = ratings.index
quantity = ratings.values

custom_colors = ["skyblue", "yellowgreen", "tomato", "blue", "red"]
plt.figure(figsize=(5, 5))
plt.pie(quantity, labels=numbers, colors=custom_colors, autopct="%1.1f%%", startangle=90)
central_circle = plt.Circle((0, 0), 0.5, color="white")
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc("font", size=12)
plt.title("Amazon Alexa Ratings", fontsize=20)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------
# Sentiment Analysis (robust to NaN / non-string values)
# -------------------------------------------------------------------
# Clean the review text: replace NaN with empty string and ensure type=str
data["verified_reviews"] = data["verified_reviews"].fillna("").astype(str)

sentiments = SentimentIntensityAnalyzer()

def safe_scores(text):
    """
    Return VADER polarity scores safely.
    If anything goes wrong, fall back to neutral.
    """
    try:
        return sentiments.polarity_scores(text)
    except Exception:
        return {"pos": 0.0, "neg": 0.0, "neu": 1.0}

scores_series = data["verified_reviews"].apply(safe_scores)

data["Positive"] = scores_series.apply(lambda d: d["pos"])
data["Negative"] = scores_series.apply(lambda d: d["neg"])
data["Neutral"]  = scores_series.apply(lambda d: d["neu"])

print("\nSample after adding sentiment columns:\n", data.head())

# -------------------------------------------------------------------
# Summing Scores & Overall Sentiment
# -------------------------------------------------------------------
x = data["Positive"].sum()
y = data["Negative"].sum()
z = data["Neutral"].sum()

def sentiment_score(a, b, c):
    if (a > b) and (a > c):
        print("\nOverall Sentiment: Positive 😊")
    elif (b > a) and (b > c):
        print("\nOverall Sentiment: Negative 😠")
    else:
        print("\nOverall Sentiment: Neutral 🙂")

sentiment_score(x, y, z)

print("\nSentiment Totals:")
print("Positive:", x)
print("Negative:", y)
print("Neutral:", z)

# -------------------------------------------------------------------
# Save results to CSV
# -------------------------------------------------------------------
data.to_csv("alexa_sentiment_results.csv", index=False)
print("\nSentiment results saved as 'alexa_sentiment_results.csv'")
