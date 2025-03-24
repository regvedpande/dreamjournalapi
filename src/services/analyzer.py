from src.models.dream import DreamInput, DreamAnalysis
from src.utils.nlp_tools import get_sentiment, extract_themes
import random

INTERPRETATIONS = {
    "positive": [
        "Your subconscious is plotting a grand adventure!",
        "Dreams like this suggest you're ready to conquer the day!",
        "A hidden optimist lives in your mind—let it shine!"
    ],
    "negative": [
        "Your brain’s throwing a dramatic party—time to RSVP with courage!",
        "A challenge lurks in your dreams; face it head-on!",
        "The chaos is just your mind rehearsing resilience."
    ],
    "neutral": [
        "Your dreams are a puzzle—piece it together slowly.",
        "A quiet mind whispers secrets—are you listening?",
        "This is your brain’s abstract art exhibit. Enjoy the mystery!"
    ]
}

async def analyze_dream(dream: DreamInput) -> DreamAnalysis:
    sentiment = get_sentiment(dream.description)
    compound_score = sentiment["compound"]
    dominant_emotion = "positive" if compound_score >= 0.05 else "negative" if compound_score <= -0.05 else "neutral"
    key_themes = extract_themes(dream.description)
    mood_influence = f" Waking up {dream.wake_mood} adds a twist to this tale." if dream.wake_mood else ""
    interpretation = random.choice(INTERPRETATIONS[dominant_emotion]) + mood_influence

    return DreamAnalysis(
        sentiment_score=round(compound_score, 2),
        dominant_emotion=dominant_emotion,
        key_themes=key_themes if key_themes else ["none detected"],
        interpretation=interpretation
    )