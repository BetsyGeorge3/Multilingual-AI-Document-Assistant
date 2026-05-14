from fastapi import APIRouter
from app.agents.query_agent import process_query

router = APIRouter()

@router.get("/query")
def query(q: str):

    result = process_query(q)

    return {
        "answer": result["answer"],
        "language": result["language"],
        "intent": result["intent"]
    }
