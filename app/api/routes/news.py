from fastapi import APIRouter
from app.pipelines.news_pipeline import run_news_pipeline

router = APIRouter()

@router.get("/important-news")
def important_news():

    articles = run_news_pipeline()

    filtered = []

    for article in articles:

        if article["importance"] >= 1:
            filtered.append(article)

    return filtered