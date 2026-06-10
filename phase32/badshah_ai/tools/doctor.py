import importlib
import sys
from badshah_ai.config.settings import settings

CORE = ["dotenv", "requests", "rich", "fastapi", "uvicorn", "streamlit", "pytest"]
OPTIONAL = ["pandas", "pypdf", "PIL", "pytesseract", "pyautogui", "playwright", "chromadb", "PyQt6"]

def check_import(name):
    try:
        importlib.import_module(name)
        return True
    except Exception:
        return False

def doctor_report():
    lines = [
        "BADSHAH-AI Doctor Report",
        f"Python: {sys.version.split()[0]}",
        f"Workspace: {settings.safe_workspace.exists()}",
        f"Exports: {settings.export_dir.exists()}",
        f"Memory dir: {settings.memory_db.parent.exists()}",
        "",
        "Core dependencies:",
    ]
    for name in CORE:
        lines.append(f"- {name}: {'OK' if check_import(name) else 'MISSING'}")
    lines.append("")
    lines.append("Optional dependencies:")
    for name in OPTIONAL:
        lines.append(f"- {name}: {'OK' if check_import(name) else 'optional missing'}")
    lines.append("")
    lines.append("Next:")
    lines.append("1. ollama pull llama3.2:1b")
    lines.append("2. installer\\START_BADSHAH_AI.bat")
    return "\n".join(lines)

if __name__ == "__main__":
    print(doctor_report())
