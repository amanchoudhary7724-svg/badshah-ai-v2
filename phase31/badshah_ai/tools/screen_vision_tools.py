from datetime import datetime
from pathlib import Path
from badshah_ai.config.settings import settings
def screen_safety():
    return "Screen Safety: local screenshot/OCR only; desktop control disabled by default."
def take_screenshot():
    try:
        import pyautogui
        out = settings.safe_workspace / "screens" / f"screen_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        pyautogui.screenshot().save(out)
        return f"Screenshot saved: {out}"
    except Exception as e:
        return "Screenshot error: " + str(e)
def image_ocr(path):
    try:
        from PIL import Image
        import pytesseract
        p = Path(path).expanduser()
        if settings.tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = settings.tesseract_cmd
        return pytesseract.image_to_string(Image.open(p)).strip() or "No text detected."
    except Exception as e:
        return "OCR error: " + str(e)
