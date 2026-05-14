from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

vector_store = None

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def create_vector_store(chunks):

    global vector_store

    texts = [doc.page_content for doc in chunks]

    vector_store = FAISS.from_texts(
        texts,
        embedding=embedding_model
    )

    return vector_store


def retrieve_docs(query, k=4):

    global vector_store

    if vector_store is None:
        raise ValueError("Upload document first")

    docs = vector_store.similarity_search(query, k=k)

    cleaned = []

    for d in docs:
        text = d.page_content.strip()

        if len(text) > 20:
            cleaned.append(d)

    return cleaned
