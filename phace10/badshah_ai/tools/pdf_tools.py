from pathlib import Path
from pypdf import PdfReader

def extract_pdf_text(path):
    p = Path(path).expanduser()
    if not p.exists():
        return "PDF not found"
    return "\n".join([(pg.extract_text() or "") for pg in PdfReader(str(p)).pages])[:12000]
