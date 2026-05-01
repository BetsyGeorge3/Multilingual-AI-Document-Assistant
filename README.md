# 🌍 Multilingual AI Document Assistant

A **Retrieval-Augmented Generation (RAG)** based AI system that allows users to upload documents and ask questions in **any language**, receiving accurate answers in their **preferred language**.

---

## 🚀 Features

* 📂 Upload documents (PDF / TXT)
* 🌐 Multilingual query support (English, Hindi, Arabic, etc.)
* 🔍 Semantic search using embeddings (FAISS)
* 🤖 Local LLM integration using Ollama (LLaMA3)
* 🔄 Automatic translation (query → English → response → user language)
* ⚡ Fast API backend with real-time responses

---

## 🧠 Architecture Overview

```
User → Upload Document → Chunking → Embeddings → FAISS Vector DB  
User Query → Translate to English → Retrieve Relevant Chunks →  
LLM (Ollama) → Generate Answer → Translate to User Language → Response
```

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Vector Database:** FAISS
* **Embeddings:** HuggingFace (Sentence Transformers)
* **LLM:** Ollama (LLaMA3)
* **Translation:** Deep Translator (Google Translate)
* **Document Parsing:** LangChain Community Loaders

---

## 📁 Project Structure

```
Multilingual-AI-Assistant/
│── app/
│   ├── main.py
│   ├── routes/
│   │   ├── upload.py
│   │   ├── query.py
│   ├── services/
│   │   ├── embedding.py
│   │   ├── retriever.py
│   │   ├── translator.py
│   │   ├── llm.py
│   ├── utils/
│   │   ├── loader.py
│   │   ├── chunking.py
│── data/
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yBetsyGeorge3/multilingual-ai-assistant.git
cd multilingual-ai-assistant
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Setup Ollama (Local LLM)

### Install Ollama

👉 https://ollama.com

### Pull Model

```bash
ollama pull llama3
```

### Run Model

```bash
ollama run llama3
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload --port 8004
```

Open in browser:

```
http://127.0.0.1:8004/docs
```

---

## 📂 API Endpoints

### 1. Upload Document

```
POST /upload
```

### 2. Query Document

```
GET /query?q=your_question
```

---

## 🧪 Example Queries

### English

```
What is the revenue in 2025?
```

### Hindi

```
2025 में कंपनी का राजस्व कितना था?
```

### Arabic

```
ما هو الإيراد في 2025؟
```

---

## 📸 Demo Flow

1. Upload financial report
2. Ask question in any language
3. System retrieves relevant context
4. LLM generates answer
5. Answer returned in user language

---

## 🔥 Key Concepts Used

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Embeddings
* Multilingual NLP
* Local LLM Inference

---

## ⚠️ Limitations

* PDF parsing depends on file quality
* Translation may fail for very long text
* No authentication / user management yet

---

## 🚀 Future Improvements

* 🔹 Add support for DOCX / Excel
* 🔹 Streaming responses (ChatGPT-like)
* 🔹 UI (React / Streamlit)
* 🔹 Conversation memory
* 🔹 Cloud deployment (AWS / Docker)

---

## 👩‍💻 Author

**Betsy George**
AI / ML Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
