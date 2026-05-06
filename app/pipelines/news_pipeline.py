from app.fetchers.rss_fetcher import fetch_rss_news
from app.processors.coin_extractor import extract_coins
from app.processors.event_classifier import classify_event
from app.processors.deduplicator import is_duplicate
from app.processors.importance_score import calculate_importance
from app.utils.save_output import save_news_output


def run_news_pipeline():

    raw_articles = fetch_rss_news()

    processed_articles = []

    existing_titles = []

    for article in raw_articles:

        title = article.get("title", "")

        if not title:
            continue

        # Skip duplicates
        if is_duplicate(title, existing_titles):
            continue

        existing_titles.append(title)

        content = article.get("content", "")

        combined_text = f"{title} {content}"

        coins = extract_coins(combined_text)

        event_type = classify_event(combined_text)

        importance = calculate_importance(
            combined_text,
            article.get("source", "")
        )

        processed_article = {
            "title": title,
            "content": content,
            "url": article.get("url", ""),
            "published": article.get("published", ""),
            "source": article.get("source", ""),
            "coins": coins,
            "event_type": event_type,
            "importance": importance
        }

        processed_articles.append(processed_article)

    # Sort by importance
    processed_articles.sort(
        key=lambda x: x["importance"],
        reverse=True
    )

    # Save output file
    save_news_output(processed_articles)

    return processed_articles