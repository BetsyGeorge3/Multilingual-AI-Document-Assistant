import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3:mini"

def generate_with_ollama(prompt: str):

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)

        data = response.json()

        # Debug safety
        if "response" not in data:
            raise Exception(f"Ollama Error: {data}")

        return data["response"]

    except Exception as e:
        return f"Error generating response: {str(e)}"
