import json
from pathlib import Path
from badshah_ai import __version__
from badshah_ai.config.settings import settings
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.tools.health_tools import health_check

def version():
    return f"BADSHAH-AI v{__version__}"

def changelog():
    p = Path(__file__).resolve().parents[2] / "CHANGELOG.md"
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
