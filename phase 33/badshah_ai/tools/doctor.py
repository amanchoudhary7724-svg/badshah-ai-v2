import importlib
import sys
from badshah_ai.config.settings import settings

CORE = ["dotenv", "requests", "rich", "fastapi", "uvicorn", "streamlit", "pytest"]

def _check(name):
    try:
        importlib.import_module(name)
        return "OK"
    except Exception:
        return "MISSING"

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
    for mod in CORE:
        lines.append(f"- {mod}: {_check(mod)}")
    return "\n".join(lines)

if __name__ == "__main__":
    print(doctor_report())
