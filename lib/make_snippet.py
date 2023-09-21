def make_snippet(str):
    words = str.split()
    first_5_words = " ".join(words[:5])
    if len(words) > 5:
        return f"{first_5_words}..."
    elif len(words) < 5:
        return words
    else:
        return first_5_words