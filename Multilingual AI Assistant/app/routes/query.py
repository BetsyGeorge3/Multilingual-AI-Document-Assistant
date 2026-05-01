from fastapi import APIRouter
from app.services.retriever import retrieve_docs, generate_answer_pipeline

router = APIRouter()

@router.get("/query")
def query(q: str):
    q_en = q  # (assuming translation step already or later)

    docs = retrieve_docs(q_en)

    answer = generate_answer_pipeline(q_en, docs)

    return {"answer": answer}
