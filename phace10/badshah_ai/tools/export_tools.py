import zipfile
from datetime import datetime
from badshah_ai.config.settings import settings, BASE_DIR

def zip_folder(source, out, exclude_dirs=None):
    exclude_dirs = exclude_dirs or {"venv","__pycache__",".git"}
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in source.rglob("*"):
            if p.is_file() and not any(part in exclude_dirs for part in p.parts):
                z.write(p, p.relative_to(source))

def export_workspace():
    out = settings.export_dir / f"workspace_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    zip_folder(settings.safe_workspace, out)
    return f"Exported: {out}"

def backup_workspace():
    out = settings.export_dir / f"backup_workspace_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    zip_folder(settings.safe_workspace, out)
    return f"Backup created: {out}"

def release_package():
    out = settings.export_dir / f"badshah_ai_v1_final_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    zip_folder(BASE_DIR, out)
    return f"Release package created: {out}"
