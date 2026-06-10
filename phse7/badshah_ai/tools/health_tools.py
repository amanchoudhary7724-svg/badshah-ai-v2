import sys
import shutil
from badshah_ai.config.settings import settings
from badshah_ai.models.ollama_client import OllamaClient

def health_check():
    lines = [
        f"Python: {sys.version.split()[0]}",
        f"Workspace exists: {settings.safe_workspace.exists()}",
        f"Exports exists: {settings.export_dir.exists()}",
        f"Memory DB parent exists: {settings.memory_db.parent.exists()}",
        f"Tesseract installed: {bool(shutil.which('tesseract')) or bool(settings.tesseract_cmd)}",
        OllamaClient().health(),
    ]
    return "\n".join(lines)

def diagnostics():
    return health_check() + "\n\nConfig checked. Use `config` to view paths."
