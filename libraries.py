import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download Vader lexicon (needed for sentiment analysis)
nltk.download('vader_lexicon')
