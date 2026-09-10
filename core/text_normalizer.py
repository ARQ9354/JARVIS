import re


# Common Hinglish / Hindi command words
COMMAND_WORDS = {
    "kholo": "open",
    "khol": "open",
    "khol do": "open",
    "chala do": "open",
    "chalao": "open",
    "start karo": "start",
    "band karo": "close",
    "band": "close",
}


def normalize_text(text):
    """
    Convert raw STT text into a simpler standardized form.
    English text is mostly kept unchanged.
    """

    text = text.lower().strip()

    # Remove common filler words
    filler_words = [
        "bhai",
        "please",
        "yaar",
        "zara",
        "mere liye"
    ]

    for word in filler_words:
        text = text.replace(word, "")

    # Normalize extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Replace common Hinglish phrases
    # Long phrases first
    replacements = {
        "khol do": "open",
        "chala do": "open",
        "start karo": "start",
        "band karo": "close",
        "khol": "open",
        "kholo": "open",
        "chalao": "open",
        "band": "close",
    }

    for old, new in replacements.items():
        text = re.sub(r"\b" + re.escape(old) + r"\b", new, text)

    return text