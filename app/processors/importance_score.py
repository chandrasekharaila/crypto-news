import re


KEYWORD_SCORES = {

    # institutions
    "blackrock": 4,
    "federal reserve": 5,
    "sec": 5,
    "coinbase": 3,
    "binance": 3,
    "kraken": 3,
    "robinhood": 3,

    # events
    "etf": 5,
    "ipo": 5,
    "acquisition": 4,
    "acquire": 4,
    "acquires": 4,
    "merger": 4,
    "buyout": 4,

    # security
    "hack": 5,
    "exploit": 5,
    "breach": 5,

    # adoption
    "institutional": 3,
    "bank": 3,
    "banks": 3,
    "wall street": 4,
    "tokenization": 3,
    "tokenized": 3,

    # funding
    "raises": 3,
    "funding": 3,
    "investment": 3,

    # regulation
    "lawmakers": 4,
    "regulation": 4,
    "bill": 3,
    "government": 3,

    # partnerships
    "partnership": 3,
    "collaboration": 3,

    # listings
    "listing": 3,
    "listed": 3,

    # upgrades
    "upgrade": 2,
    "mainnet": 2
}


SOURCE_SCORES = {
    "CoinDesk": 3,
    "Cointelegraph": 2
}


def calculate_importance(text, source=""):

    text = text.lower()

    score = 1

    # keyword scoring
    for keyword, weight in KEYWORD_SCORES.items():

        pattern = r"\b" + re.escape(keyword) + r"\b"

        if re.search(pattern, text):
            score += weight

    # source reliability bonus
    for source_name, source_weight in SOURCE_SCORES.items():

        if source_name.lower() in source.lower():
            score += source_weight

    # cap score at 10
    return min(score, 10)