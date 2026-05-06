COINS = [
    "bitcoin",
    "ethereum",
    "solana",
    "xrp",
    "bnb",
    "dogecoin"
]

def extract_coins(text):

    text = text.lower()

    found_coins = []

    for coin in COINS:

        if coin in text:
            found_coins.append(coin)

    return found_coins