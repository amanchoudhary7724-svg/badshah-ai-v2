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
        self.active_role = "default"

    def model_for(self, role_or_prompt="default"):
        key = (role_or_prompt or "default").lower().strip()
        if key in self.role_models:
            return self.role_models[key]
        if any(w in key for w in ["code", "python", "javascript", "bug", "fix", "function"]):
            return self.role_models["coding"]
        if any(w in key for w in ["explain", "plan", "strategy", "deep", "analyze"]):
            return self.role_models["smart"]
        if len(key) < 80:
            return self.role_models["fast"]
        return self.role_models["default"]

    def list_models_config(self):
        return "\n".join([f"{role}: {model}" for role, model in self.role_models.items()])

    def installed_models(self):
        try:
            r = requests.get(f"{settings.ollama_url.rstrip('/')}/api/tags", timeout=10)
            r.raise_for_status()
            return [m.get("name", "unknown") for m in r.json().get("models", [])]
        except Exception:
            return []

    def health(self):
        installed = self.installed_models()
        if not installed:
            return "Ollama not connected or no models found."
        lines = ["Installed models:"] + installed + ["", "Configured roles:", self.list_models_config()]
        return "\n".join(lines)

    def generate(self, prompt, role="default"):
        model = self.model_for(role)
        result = self._generate_with_model(prompt, model)
        if result.startswith("LLM error") and model != settings.fallback_model:
            fallback_result = self._generate_with_model(prompt, settings.fallback_model)
            return f"[Fallback: {settings.fallback_model}]\n{fallback_result}"
        return result

    def _generate_with_model(self, prompt, model):
        try:
            r = requests.post(
                f"{settings.ollama_url.rstrip('/')}/api/generate",
                json={"model": model, "prompt": prompt, "stream": False},
                timeout=120,
            )
            r.raise_for_status()
            return r.json().get("response", "").strip() or "Empty response."
        except Exception as e:
            return f"LLM error with model {model}: {e}"
