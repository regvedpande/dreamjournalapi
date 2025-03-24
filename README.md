
# Dream Journal Sentiment Analyzer API

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/regvedpande/dreamjournalapi)

## Overview

The **Dream Journal Sentiment Analyzer API** is a FastAPI-based application that analyzes user-submitted dream descriptions. It uses natural language processing (NLP) to detect sentiment, extract key themes, and provide quirky interpretations of dreams. This project showcases modern Python development with FastAPI, Pydantic for data validation, and NLP libraries like TextBlob and NLTK.

## Features

- **Sentiment Analysis**: Detects the emotional tone of your dream (positive, negative, or neutral).
- **Theme Extraction**: Identifies key themes (nouns) in your dream description.
- **Quirky Interpretations**: Generates creative interpretations based on sentiment and mood.
- **FastAPI Framework**: Provides a fast, async API with automatic Swagger UI documentation.
- **Input Validation**: Uses Pydantic to ensure valid user inputs.

## Technologies Used

- **Python**: Core programming language.
- **FastAPI**: Framework for building the API.
- **TextBlob**: For theme extraction and POS tagging.
- **NLTK**: For sentiment analysis using VADER.
- **Pydantic**: For request and response validation.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/regvedpande/dreamjournalapi.git
   cd dreamjournalapi
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK and TextBlob Data**:
   ```bash
   python -m nltk.downloader vader_lexicon punkt
   python -m textblob.download_corpora
   ```

4. **Run the Application**:
   - On Windows:
     ```bash
     run.bat
     ```
   - Or directly:
     ```bash
     uvicorn src.main:app --reload
     ```

5. **Access the API**:
   Open your browser to `http://127.0.0.1:8000/docs` to explore the API using Swagger UI.

## Usage

### Endpoint: `POST /analyze-dream`

Analyze a dream description and get sentiment, themes, and an interpretation.

#### Example Request
```bash
curl -X POST "http://127.0.0.1:8000/analyze-dream" \
-H "Content-Type: application/json" \
-d '{"description": "I flew over a forest with talking trees.", "wake_mood": "happy"}'
```

#### Example Response
```json
{
    "sentiment_score": 0.0,
    "dominant_emotion": "neutral",
    "key_themes": ["forest", "trees"],
    "interpretation": "Your dreams are a puzzle—piece it together slowly. Waking up happy adds a twist to this tale."
}
```

## Contact

For questions or feedback, reach out to me at [regregd@outlook.com](mailto:regregd@outlook.com).

---

Happy dreaming! 🌙
