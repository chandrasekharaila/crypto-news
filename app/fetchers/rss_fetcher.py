import feedparser


RSS_FEEDS = [

    {
        "name": "CoinDesk",
        "url": "https://www.coindesk.com/arc/outboundfeeds/rss/"
    },

    {
        "name": "Cointelegraph",
        "url": "https://cointelegraph.com/rss"
    },

    {
        "name": "Decrypt",
        "url": "https://decrypt.co/feed"
    },

    {
        "name": "The Block",
        "url": "https://www.theblock.co/rss.xml"
    },

    {
        "name": "CryptoSlate",
        "url": "https://cryptoslate.com/feed/"
    }
]


def fetch_rss_news():

    all_articles = []

    for source in RSS_FEEDS:

        feed = feedparser.parse(source["url"])

        for entry in feed.entries:

            article = {
                "title": entry.get("title", ""),
                "content": entry.get("summary", ""),
                "url": entry.get("link", ""),
                "published": entry.get("published", ""),
                "source": source["name"]
            }

            all_articles.append(article)

    return all_articles