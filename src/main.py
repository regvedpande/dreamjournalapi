from fastapi import FastAPI, HTTPException
from src.models.dream import DreamInput, DreamAnalysis
from src.services.analyzer import analyze_dream

app = FastAPI(
    title="Dream Journal Sentiment Analyzer API",
    description="Analyze your dreams and get quirky insights!",
    version="1.0.0"
)

@app.post("/analyze-dream", response_model=DreamAnalysis)
async def analyze_dream_endpoint(dream: DreamInput):
    if not dream.description.strip():
        raise HTTPException(status_code=400, detail="Dream description cannot be empty.")
    return await analyze_dream(dream)

@app.get("/")
async def root():
    return {"message": "Welcome to the Dream Journal Sentiment Analyzer API! Use /docs to explore."}