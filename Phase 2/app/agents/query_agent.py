from app.utils.language import detect_language
from app.services.translate import to_english, from_english
from app.services.retrieval import retrieve_docs
from app.services.context import build_context
from app.services.llm import generate_with_ollama
from app.services.intent import detect_intent
from app.services.response import build_prompt

def process_query(query: str):

    # 1. Detect language
    lang = detect_language(query)

    # 2. Translate to English
    query_en = to_english(query, source_lang="auto")

    # 3. Intent detection
    intent = detect_intent(query_en)

    # 4. Retrieve docs
    docs = retrieve_docs(query_en)

    # 5. Build context (improved)
    context = build_context(docs)

    # 6. Prompt engineering
    prompt = build_prompt(query_en, context, intent)

    # 7. LLM response
    answer_en = generate_with_ollama(prompt)

    # 8. Translate back
    answer = from_english(answer_en, lang)

    return {
        "language": lang,
        "intent": intent,
        "answer": answer
    }
