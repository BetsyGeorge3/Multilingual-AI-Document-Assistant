import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_with_ollama(prompt: str):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    # 🔥 DEBUG SAFETY
    if "response" not in data:
        raise Exception(f"Ollama Error: {data}")

    return data["response"]
