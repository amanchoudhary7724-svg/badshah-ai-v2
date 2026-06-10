import requests
from badshah_ai.config.settings import settings
class LLMRouter:
    def __init__(self):
        self.role_models = {
            "default": settings.default_model,
            "fast": settings.fast_model,
            "coding": settings.coding_model,
            "smart": settings.smart_model,
            "fallback": settings.fallback_model,
        }
    def list_models_config(self):
        return "\n".join([f"{r}: {m}" for r, m in self.role_models.items()])
    def generate(self, prompt, role="default"):
        model = self.role_models.get(role, self.role_models["default"])
        try:
            r = requests.post(f"{settings.ollama_url.rstrip('/')}/api/generate", json={"model": model, "prompt": prompt, "stream": False}, timeout=120)
            r.raise_for_status()
            return r.json().get("response", "").strip() or "Empty response."
        except Exception as e:
            return "LLM error: " + str(e)
