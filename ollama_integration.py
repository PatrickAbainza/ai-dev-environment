import os
import requests

OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "your_ollama_api_key_here")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")  # Example URL for local Ollama server

def query_ollama(prompt: str) -> dict:
    """Send a query to the local Ollama server using the deepseek-r1 model."""
    endpoint = f"{OLLAMA_URL}/query"
    headers = {"Authorization": f"Bearer {OLLAMA_API_KEY}"}
    payload = {"prompt": prompt, "model": "deepseek-r1"}
    try:
        response = requests.post(endpoint, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    prompt = "Provide a sample query for deepseek-r1."
    result = query_ollama(prompt)
    print("Ollama Query Result:", result)
