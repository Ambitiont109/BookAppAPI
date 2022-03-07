def string_to_bool(text):
    """
    Convert 'True'|'true' to Bool(True)
    """
    text = text.lower()
    if text == "true":
        return True
    return False