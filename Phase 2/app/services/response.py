def build_prompt(query, context, intent):

    base_prompt = f"""
You are an enterprise multilingual document AI assistant.

STRICT RULES:
1. Answer ONLY from context
2. Never invent information
3. If unsure, say:
   "Not found in documents"
4. Keep answers factual
5. Use bullet points when helpful

Intent: {intent}

Context:
{context}

Question:
{query}

Answer:
"""

    return base_prompt
