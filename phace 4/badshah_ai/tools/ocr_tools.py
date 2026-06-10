from pathlib import Path
from PIL import Image
import pytesseract
from badshah_ai.config.settings import settings
def extract_image_text(path):
    p=Path(path).expanduser()
    if not p.exists(): return "Image not found"
    if settings.tesseract_cmd: pytesseract.pytesseract.tesseract_cmd=settings.tesseract_cmd
    try: return pytesseract.image_to_string(Image.open(p)).strip() or "No text detected."
    except Exception as e: return "OCR error: "+str(e)
