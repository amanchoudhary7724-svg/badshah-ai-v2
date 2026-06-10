from badshah_ai.config.settings import settings

def create_website(name="portfolio"):
    name = "".join(c for c in name.lower().replace(" ","_") if c.isalnum() or c in "_-") or "portfolio"
    folder = settings.safe_workspace / name
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "index.html").write_text("<h1>BADSHAH Website</h1><p>Ready.</p>", encoding="utf-8")
    (folder / "style.css").write_text("body{font-family:Arial;background:#0f172a;color:white;text-align:center;padding:80px}", encoding="utf-8")
    return f"Website created: {folder}"
