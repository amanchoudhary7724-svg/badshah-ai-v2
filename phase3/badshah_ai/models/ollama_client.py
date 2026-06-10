import logging
import requests
from badshah_ai.config.settings import settings

logger = logging.getLogger(__name__)

class OllamaClient:
    def __init__(self, base_url: str | None = None, model: str | None = None) -> None:
        self.base_url = (base_url or settings.ollama_url).rstrip("/")
        self.model = model or settings.default_model

    def generate(self, prompt: str) -> str:
        url = f"{self.base_url}/api/generate"
        payload = {"model": self.model, "prompt": prompt, "stream": False}
        try:
            response = requests.post(url, json=payload, timeout=120)
            response.raise_for_status()
            data = response.json()
            return data.get("response", "").strip() or "Model ne empty response diya."
        except requests.RequestException as exc:
            logger.exception("Ollama request failed")
            return (
                "Ollama connect nahi ho pa raha. Pehle Ollama install/run karo aur model pull karo: "
                "`ollama pull llama3.2:1b`. Error: " + str(exc)
            )
