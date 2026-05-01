from deep_translator import GoogleTranslator


def to_english(text: str, source_lang: str = "auto"):
    try:
        return GoogleTranslator(source=source_lang, target="en").translate(text)
    except Exception:
        return text


def from_english(text: str, target_lang: str):
    try:
        if target_lang == "en":
            return text

        # limit size to avoid crash
        text = text[:500]

        return GoogleTranslator(source="en", target=target_lang).translate(text)

    except Exception:
        return text  # fallback
