import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Sample data - you can replace this with real news headlines or load from a CSV file
data = {
    "headline": [
        "Stock market hits an all-time high",
        "Company reports losses due to economic downturn",
        "Positive earnings report boosts investor confidence",
        "Stock prices fall amid trade war concerns",
        "Tech stocks soar as new product is launched"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Function to analyze sentiment of each headline
def analyze_sentiment(headline):
    score = analyzer.polarity_scores(headline)
    compound_score = score['compound']
    if compound_score >= 0.05:
        sentiment = "Positive"
    elif compound_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return compound_score, sentiment

# Apply sentiment analysis to each headline
df['Compound Score'], df['Sentiment'] = zip(*df['headline'].apply(analyze_sentiment))

# Display the DataFrame with sentiment results
print(df)
