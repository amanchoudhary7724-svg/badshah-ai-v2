import zipfile
from datetime import datetime
from badshah_ai.config.settings import settings, BASE_DIR

def release_package():
    out = settings.export_dir / f"badshah_ai_v1_1_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in BASE_DIR.rglob("*"):
            if p.is_file() and "venv" not in p.parts and ".git" not in p.parts:
                z.write(p, p.relative_to(BASE_DIR))
    return f"Release package created: {out}"
