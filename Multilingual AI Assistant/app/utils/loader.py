import os
from langchain_community.document_loaders import PyPDFLoader

def load_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        return [doc.page_content for doc in docs]

    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return [f.read()]

    else:
        raise ValueError("Unsupported file type")
