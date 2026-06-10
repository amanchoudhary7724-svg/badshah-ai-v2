import zipfile
from datetime import datetime
from badshah_ai.config.settings import settings, BASE_DIR
def zip_dir(source, out):
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in source.rglob("*"):
            if p.is_file() and "venv" not in p.parts and ".git" not in p.parts and "__pycache__" not in p.parts:
                z.write(p, p.relative_to(source))
def export_workspace():
    out = settings.export_dir / f"workspace_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"; zip_dir(settings.safe_workspace, out); return f"Workspace exported: {out}"
def release_package():
    out = settings.export_dir / f"badshah_ai_v1_8_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"; zip_dir(BASE_DIR, out); return f"Release package created: {out}"
