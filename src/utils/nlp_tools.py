from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def get_sentiment(text: str) -> dict:
    return sia.polarity_scores(text)

def extract_themes(text: str) -> list[str]:
    blob = TextBlob(text)
    nouns = [word for (word, pos) in blob.tags if pos.startswith("NN")]
    return list(set(nouns))[:5]