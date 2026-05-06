import json
import os


def save_news_output(data, filename="crypto_news.json"):

    # create output folder if not exists
    os.makedirs("output", exist_ok=True)

    filepath = os.path.join("output", filename)

    with open(filepath, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"Saved news to {filepath}")