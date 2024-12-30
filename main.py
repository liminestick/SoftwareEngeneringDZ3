from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Загрузка модели анализа тональности
sentiment_model = pipeline("sentiment-analysis")

# Инициализация FastAPI
app = FastAPI()


# Класс для входных данных
class SentimentInput(BaseModel):
    text: str


@app.get("/")
def root():
    logging.info("GET request to root endpoint")
    return {"message": "Добро пожаловать в API для анализа тональности!"}


@app.post("/analyze/")
def analyze_sentiment(data: SentimentInput):
    # Проверка на пустой текст
    if not data.text.strip():
        logging.warning("Received empty text")
        raise HTTPException(status_code=400, detail="Text must not be empty")

    logging.info(f"Analyzing sentiment for text: {data.text}")

    # Анализ тональности
    result = sentiment_model(data.text)

    logging.info(f"Sentiment analysis result: {result}")

    return {"text": data.text, "analysis": result}
