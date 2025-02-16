
# Import SentimentIntensityAnalyzer class
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



# Create an object of SentimentIntensityAnalyzer class
analyzer = SentimentIntensityAnalyzer()
t='AAPL is worst and bad stock never invest  '
print(t)
a=analyzer.polarity_scores(t)
print(a)