from badshah_ai.config.settings import settings

def create_static_website(name="portfolio"):
    name = "".join(c for c in name.replace(" ","_").lower() if c.isalnum() or c in "_-") or "portfolio"
    folder = settings.safe_workspace / name
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "index.html").write_text("<h1>BADSHAH Website</h1>", encoding="utf-8")
    return f"Website created: {folder}"
