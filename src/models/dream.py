from pydantic import BaseModel, Field
from typing import Optional, List

class DreamInput(BaseModel):
    description: str = Field(..., min_length=10, description="Your dream description")
    wake_mood: Optional[str] = Field(default=None, description="Mood upon waking (e.g., happy, confused)")

class DreamAnalysis(BaseModel):
    sentiment_score: float
    dominant_emotion: str
    key_themes: List[str]
    interpretation: str