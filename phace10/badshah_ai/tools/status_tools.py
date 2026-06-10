import json
from pathlib import Path
from badshah_ai import __version__
from badshah_ai.config.settings import settings, BASE_DIR
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.tools.health_tools import health_check

def version():
    return f"BADSHAH-AI v{__version__}"

def changelog():
    p = BASE_DIR / "CHANGELOG.md"
    return p.read_text(encoding="utf-8") if p.exists() else "CHANGELOG.md not found."

def status_report():
    data = {
        "version": __version__,
        "plugins": len(list_plugins()),
        "workspace": str(settings.safe_workspace),
        "exports": str(settings.export_dir),
        "health": health_check(),
    }
    return json.dumps(data, indent=2)

def command_suggestions():
    return "Try: help | validate env | health check | create website portfolio | release package | self modify add feature"

def show_logs(max_chars=4000):
    p = settings.log_file
    if not p.exists():
        return "No log file found."
    text = p.read_text(encoding="utf-8", errors="ignore")
    return text[-max_chars:] if text else "Log file is empty."
