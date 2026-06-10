from pathlib import Path

def pdf_text(path):
    try:
        from pypdf import PdfReader
        p = Path(path).expanduser()
        if not p.exists(): return "PDF not found"
        return "\n".join([(pg.extract_text() or "") for pg in PdfReader(str(p)).pages])[:12000]
    except Exception as e:
        return "PDF error: " + str(e)

def excel_summary(path):
    try:
        import pandas as pd
        p = Path(path).expanduser()
        if not p.exists(): return "Excel/CSV not found"
        df = pd.read_csv(p) if p.suffix.lower() == ".csv" else pd.read_excel(p)
        return f"Rows: {len(df)}\nColumns: {len(df.columns)}\n{df.head().to_string(index=False)}"
    except Exception as e:
        return "Excel error: " + str(e)

def ocr_image(path, tesseract_cmd=""):
    try:
        from PIL import Image
        import pytesseract
        p = Path(path).expanduser()
        if not p.exists(): return "Image not found"
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
        return pytesseract.image_to_string(Image.open(p)).strip() or "No text detected."
    except Exception as e:
        return "OCR error: " + str(e)
