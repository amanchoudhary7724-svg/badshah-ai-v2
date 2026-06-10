from pathlib import Path
from pypdf import PdfReader

def extract_pdf_text(path):
    p = Path(path).expanduser()
    if not p.exists():
        return "PDF not found"
    txt = []
    for i,page in enumerate(PdfReader(str(p)).pages,1):
        txt.append(f"--- Page {i} ---\n{page.extract_text() or ''}")
    return "\n".join(txt)[:12000]
