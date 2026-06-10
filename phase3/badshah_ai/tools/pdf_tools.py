from pathlib import Path
from pypdf import PdfReader

def extract_pdf_text(path: str, max_chars: int = 12000) -> str:
    pdf_path = Path(path).expanduser()
    if not pdf_path.exists():
        return f"PDF file not found: {pdf_path}"
    reader = PdfReader(str(pdf_path))
    parts = []
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        parts.append(f"--- Page {i} ---\n{text}")
        if sum(len(p) for p in parts) >= max_chars:
            break
    output = "\n\n".join(parts).strip()
    return output[:max_chars] if output else "No readable text found in PDF."
