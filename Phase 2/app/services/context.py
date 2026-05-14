def build_context(docs):
    seen = set()
    cleaned = []

    for d in docs:
        text = d.page_content.strip()

        if text not in seen:
            seen.add(text)
            cleaned.append(text)

    return "\n\n".join(cleaned)[:2000]
