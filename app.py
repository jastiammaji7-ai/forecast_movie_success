from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI()

# allow calls from Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

analyzer = SentimentIntensityAnalyzer()

class Review(BaseModel):
    movie: str
    review: str

@app.get("/")
def home():
    return {"message": "Backend is running successfully"}

@app.post("/predict")
def predict_sentiment(data: Review):
    score = analyzer.polarity_scores(data.review)["compound"]
    label = "Hit" if score > 0 else "Average"
    confidence = round(abs(score), 2)
    return {
        "movie": data.movie,
        "prediction": label,
        "confidence": confidence
    }
