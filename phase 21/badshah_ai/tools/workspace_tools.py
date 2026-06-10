from badshah_ai.config.settings import settings
def safe_path(name):
    base = settings.safe_workspace.resolve()
    target = (base / name).resolve()
    if not str(target).startswith(str(base)):
        raise ValueError("Unsafe path blocked")
    return target
def write_file(name, content):
    p = safe_path(name); p.parent.mkdir(parents=True, exist_ok=True); p.write_text(content, encoding="utf-8"); return f"Saved: {p}"
def read_file(name):
    p = safe_path(name); return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else f"Not found: {p}"
def create_website(name="portfolio"):
    name = "".join(c for c in name.lower().replace(" ","_") if c.isalnum() or c in "_-") or "portfolio"
    write_file(f"{name}/index.html", "<h1>BADSHAH Website</h1><p>VS Code Agent Ready.</p>")
    write_file(f"{name}/style.css", "body{font-family:Arial;background:#0f172a;color:white;text-align:center;padding:80px}")
    return f"Website created: workspace/{name}"
