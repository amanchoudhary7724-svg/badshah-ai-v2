import importlib
import sys
from badshah_ai.config.settings import settings

def doctor_report():
    mods = ["dotenv", "requests", "rich", "fastapi", "uvicorn", "streamlit", "pytest"]
    lines = [
        "BADSHAH-AI Doctor Report",
        f"Python: {sys.version.split()[0]}",
        f"Workspace: {settings.safe_workspace.exists()}",
        f"Exports: {settings.export_dir.exists()}",
        f"Memory dir: {settings.memory_db.parent.exists()}",
        "",
        "Dependencies:",
    ]
    for m in mods:
        try:
            importlib.import_module(m)
            lines.append(f"- {m}: OK")
        except Exception:
            lines.append(f"- {m}: MISSING")
    return "\n".join(lines)

if __name__ == "__main__":
    print(doctor_report())
