import zipfile
from datetime import datetime
from badshah_ai.config.settings import settings

def export_workspace():
    out = settings.export_dir / f"workspace_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
        for p in settings.safe_workspace.rglob("*"):
            if p.is_file():
                z.write(p, p.relative_to(settings.safe_workspace))
    return f"Exported: {out}"
