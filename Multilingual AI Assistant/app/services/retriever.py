from langchain_community.vectorstores import FAISS
from app.services.embeddings import get_embeddings
from app.services.llm import generate_with_ollama

vector_store = None


def create_vector_store(docs):
    global vector_store

    embeddings = get_embeddings()
    vector_store = FAISS.from_documents(docs, embeddings)

    return vector_store


def retrieve_docs(query, k=4):
    global vector_store

    if vector_store is None:
        raise ValueError("Vector store not initialized. Upload a document first.")

    return vector_store.similarity_search(query, k=k)


def generate_answer_pipeline(query, docs):
    context = "\n".join([d.page_content for d in docs])[:2000]

    prompt = f"""
You are a helpful AI assistant.

Use ONLY the context below:

{context}

Question:
{query}

Answer clearly and concisely.
"""

    return generate_with_ollama(prompt)
