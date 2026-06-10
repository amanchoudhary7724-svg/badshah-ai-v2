import sys
import shutil
from badshah_ai.config.settings import settings, BASE_DIR
from badshah_ai.models.ollama_client import OllamaClient

def validate_env():
    env_path = BASE_DIR / ".env"
    issues = []
    if not env_path.exists():
        issues.append(".env missing. Copy .env.example to .env")
    if not settings.ollama_url.startswith("http"):
        issues.append("OLLAMA_URL should start with http")
    if not settings.default_model:
        issues.append("DEFAULT_MODEL is empty")
    for folder in [settings.safe_workspace, settings.export_dir, settings.memory_db.parent]:
        if not folder.exists():
            issues.append(f"Missing folder: {folder}")
    return "ENV OK" if not issues else "ENV issues:\n" + "\n".join("- " + i for i in issues)

def health_check():
    return "\n".join([
        f"Python: {sys.version.split()[0]}",
        f"Workspace exists: {settings.safe_workspace.exists()}",
        f"Exports exists: {settings.export_dir.exists()}",
        f"Memory DB parent exists: {settings.memory_db.parent.exists()}",
        f"Tesseract installed: {bool(shutil.which('tesseract')) or bool(settings.tesseract_cmd)}",
        OllamaClient().health(),
    ])

def diagnostics():
    return health_check() + "\n\n" + validate_env()

def smoke_test():
    checks = [
        ("settings", settings.app_name == "BADSHAH-AI"),
        ("workspace", settings.safe_workspace.exists()),
        ("exports", settings.export_dir.exists()),
        ("memory_parent", settings.memory_db.parent.exists()),
    ]
    failed = [name for name, ok in checks if not ok]
    return "SMOKE TEST OK" if not failed else "SMOKE TEST FAILED: " + ", ".join(failed)
