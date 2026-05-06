EVENT_KEYWORDS = {

    "acquisition": [
        "acquire",
        "acquires",
        "acquisition",
        "buyout",
        "merger"
    ],

    "funding": [
        "raises",
        "funding",
        "series a",
        "series b",
        "investment"
    ],

    "etf": [
        "etf"
    ],

    "hack": [
        "hack",
        "exploit",
        "breach"
    ],

    "partnership": [
        "partnership",
        "collaboration"
    ],

    "ipo": [
        "ipo",
        "public offering"
    ],

    "regulation": [
        "sec",
        "regulation",
        "bill",
        "lawmakers",
        "government"
    ],

    "institutional_adoption": [
        "bank",
        "institution",
        "wall street",
        "adoption"
    ],

    "tokenization": [
        "tokenization",
        "tokenized"
    ],

    "listing": [
        "listing",
        "listed"
    ],

    "upgrade": [
        "upgrade",
        "mainnet"
    ]
}

def classify_event(text):

    text = text.lower()

    for event_type, keywords in EVENT_KEYWORDS.items():

        for keyword in keywords:

            if keyword in text:
                return event_type

    return "general"