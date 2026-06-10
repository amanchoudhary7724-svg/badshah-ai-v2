import requests
from badshah_ai.config.settings import settings
class OllamaClient:
    def generate(self, prompt: str) -> str:
        try:
            r = requests.post(
                f"{settings.ollama_url.rstrip('/')}/api/generate",
                json={"model": settings.default_model, "prompt": prompt, "stream": False},
                timeout=120,
            )
            r.raise_for_status()
            return r.json().get("response", "").strip() or "Empty response."
        except Exception as e:
            return "Ollama connect nahi ho pa raha. Run: ollama pull llama3.2:1b. Error: " + str(e)
    def health(self):
        try:
            r = requests.get(f"{settings.ollama_url.rstrip('/')}/api/tags", timeout=10)
            r.raise_for_status()
            return "Ollama OK"
        except Exception as e:
            return "Ollama not connected: " + str(e)
