from badshah_ai.config.settings import settings
def safe_path(name):
    base = settings.safe_workspace.resolve()
    target = (base / name).resolve()
    if not str(target).startswith(str(base)):
        raise ValueError("Unsafe path blocked")
    return target
def create_website(name="portfolio"):
    name = "".join(c for c in name.lower().replace(" ","_") if c.isalnum() or c in "_-") or "portfolio"
    p = safe_path(f"{name}/index.html")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("<h1>BADSHAH Plugin Marketplace Ready</h1>", encoding="utf-8")
    return f"Website created: workspace/{name}"
