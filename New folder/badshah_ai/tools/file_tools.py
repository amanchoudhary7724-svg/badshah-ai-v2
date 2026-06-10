from pathlib import Path
from badshah_ai.config.settings import settings

def safe_path(relative_path: str) -> Path:
    base = settings.safe_workspace.resolve()
    target = (base / relative_path).resolve()
    if not str(target).startswith(str(base)):
        raise ValueError("Unsafe path blocked. Files can only be accessed inside workspace/.")
    return target

def write_text_file(relative_path: str, content: str) -> str:
    target = safe_path(relative_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return f"File saved: {target}"

def read_text_file(relative_path: str) -> str:
    target = safe_path(relative_path)
    if not target.exists():
        return f"File not found: {target}"
    return target.read_text(encoding="utf-8", errors="ignore")
