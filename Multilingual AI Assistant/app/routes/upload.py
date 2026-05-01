from fastapi import APIRouter, UploadFile
import shutil
from app.utils.loader import load_file
from app.utils.chunking import chunk_text
from app.services.retriever import create_vector_store
from langchain_core.documents import Document
import os

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile):
    os.makedirs("data", exist_ok=True)

    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    pages = load_file(file_path)
    text = " ".join(pages)

    chunks = chunk_text(text)

    # convert to LangChain format
    docs = [Document(page_content=chunk) for chunk in chunks]

    create_vector_store(docs)

    return {"message": "Document processed successfully"}
