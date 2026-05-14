from deep_translator import GoogleTranslator

def to_english(text: str, source_lang="auto"):
    try:
        return GoogleTranslator(source=source_lang, target="en").translate(text)
    except:
        return text


def from_english(text: str, target_lang: str):

    if target_lang == "en":
        return text

    try:
        return GoogleTranslator(source="en", target=target_lang).translate(text[:800])
    except:
        return text
