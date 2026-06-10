from badshah_ai.config.settings import settings

def safe_path(p):
    base = settings.safe_workspace.resolve()
    target = (base / p).resolve()
    if not str(target).startswith(str(base)):
        raise ValueError("Unsafe path")
    return target

def write_text_file(path, content):
    p = safe_path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return f"Saved: {p}"

def read_text_file(path):
    p = safe_path(path)
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else f"Not found: {p}"
