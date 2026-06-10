from pathlib import Path
from PIL import Image
import pytesseract
from badshah_ai.config.settings import settings

def extract_image_text(path: str) -> str:
    image_path = Path(path).expanduser()
    if not image_path.exists():
        return f"Image not found: {image_path}"

    if settings.tesseract_cmd:
        pytesseract.pytesseract.tesseract_cmd = settings.tesseract_cmd

    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        return text.strip() or "No text detected in image."
    except Exception as exc:
        return (
            "OCR failed. Tesseract install/config check karo. "
            "Windows path example: TESSERACT_CMD=C:\\Program Files\\Tesseract-OCR\\tesseract.exe. "
            f"Error: {exc}"
        )
