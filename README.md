# Alexa-Sentiment-Analysis
Amazon Alexa Sentiment Analysis uses customer reviews to evaluate user opinions on Alexa devices. By analyzing text feedback with NLTK's VADER, it identifies positive, negative, and neutral sentiments, helping understand overall customer satisfaction and improve Alexa’s user experience.

Features:-
- Visualize Amazon Alexa rating distribution using charts
- Perform sentiment analysis on verified reviews
- Identify overall customer sentiment (Positive / Negative / Neutral)
- Save results to CSV for easy access and reporting
- Clean and structured Python code for easy execution

Project Structure:-

<img width="437" height="131" alt="Screenshot 2025-08-26 231737" src="https://github.com/user-attachments/assets/58b13f78-ed21-4021-9728-421848bbf58b" />

Usage:-
Run the Python script:
python sentiment_analysis.py
- Generates charts for rating distribution.
- Calculates positive, negative, and neutral sentiment scores.
- Displays the overall sentiment.
- Saves results to alexa_sentiment_results.csv

Sample Output / Visualization:-
1. Pie Chart of Ratings:
<img width="500" height="500" alt="Output" src="https://github.com/user-attachments/assets/66658826-a6a6-408d-bc8a-2ddb42a8e5c9" />


2. Sentiment Scores Example:

Overall Sentiment: Neutral 🙂

Positive:  1363.30

Negative:   82.78

Neutral:   1688.56

3. CSV Output:

alexa_sentiment_results.csv contains:-
| rating | date      | variation     | verified\_reviews | feedback | Positive | Negative | Neutral |
| ------ | --------- | ------------- | ----------------- | -------- | -------- | -------- | ------- |
| 5      | 31-Jul-18 | Black Dot 2nd | Love my Echo!     | 1        | 0.636    | 0.0      | 0.364   |
| 5      | 31-Jul-18 | Black Dot 2nd | Loved it!         | 1        | 0.636    | 0.0      | 0.364   |


