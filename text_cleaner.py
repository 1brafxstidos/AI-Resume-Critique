import re


def clean_text(text):
    """
    Clean and normalize extracted text.
    """

    # Replace multiple spaces with one space
    text = re.sub(r"\s+", " ", text)

    # Remove excessive dots
    text = re.sub(r"\.{2,}", ".", text)

    # Remove leading and trailing spaces
    text = text.strip()

    return text