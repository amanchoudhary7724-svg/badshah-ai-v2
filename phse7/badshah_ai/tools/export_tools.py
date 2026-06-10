import zipfile
from datetime import datetime
from badshah_ai.config.settings import settings

def zip_folder(source, out):
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
        for p in source.rglob("*"):
            if p.is_file():
                z.write(p, p.relative_to(source))

def export_workspace():
    out = settings.export_dir / f"workspace_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    zip_folder(settings.safe_workspace, out)
    return f"Exported: {out}"

def backup_workspace():
    out = settings.export_dir / f"backup_workspace_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    zip_folder(settings.safe_workspace, out)
    return f"Backup created: {out}"
