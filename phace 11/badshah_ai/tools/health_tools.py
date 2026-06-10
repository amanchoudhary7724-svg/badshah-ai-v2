from badshah_ai.config.settings import settings
from badshah_ai.models.ollama_client import OllamaClient

def validate_env():
    return "ENV OK" if settings.ollama_url.startswith("http") else "ENV issue: OLLAMA_URL invalid"

def health_check():
    return "\n".join([
        f"Workspace: {settings.safe_workspace.exists()}",
        f"Exports: {settings.export_dir.exists()}",
        OllamaClient().health(),
    ])

def smoke_test():
    return "SMOKE TEST OK"
