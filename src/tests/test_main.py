from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_analyze_dream():
    response = client.post("/analyze-dream", json={"description": "I flew over a forest.", "wake_mood": "happy"})
    assert response.status_code == 200
    assert "sentiment_score" in response.json()