import sys
from badshah_ai.config.settings import settings
from badshah_ai.models.ollama_client import OllamaClient

def health_check():
    lines = [
        f"Python: {sys.version.split()[0]}",
        f"Workspace: {settings.safe_workspace}",
        f"Memory DB: {settings.memory_db}",
        f"Task DB: {settings.task_db}",
        OllamaClient().health(),
    ]
    return "\n".join(lines)
