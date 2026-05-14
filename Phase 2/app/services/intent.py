def detect_intent(query: str) -> str:
    q = query.lower()

    if "compliance" in q or "violation" in q:
        return "compliance_check"
    elif "summarize" in q:
        return "summary"
    else:
        return "general"
