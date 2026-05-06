from rapidfuzz import fuzz

def is_duplicate(title, existing_titles):

    for existing_title in existing_titles:

        similarity = fuzz.ratio(
            title.lower(),
            existing_title.lower()
        )

        if similarity > 90:
            return True

    return False