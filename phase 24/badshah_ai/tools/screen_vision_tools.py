from datetime import datetime
from pathlib import Path
from badshah_ai.config.settings import settings

SAFE_ACTIONS = {
    "open notepad": "notepad.exe",
    "open calculator": "calc.exe",
    "open paint": "mspaint.exe",
}

def screen_safety():
    return '''Screen Safety:
- Screenshot/OCR allowed locally
- Desktop control disabled by default
- Only whitelisted app-open actions
- No password capture
- No payment/destructive actions
'''

def take_screenshot():
    try:
        import pyautogui
        out_dir = settings.safe_workspace / "screens"
        out_dir.mkdir(parents=True, exist_ok=True)
        out = out_dir / f"screen_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        img = pyautogui.screenshot()
        img.save(out)
        return f"Screenshot saved: {out}"
    except Exception as e:
        return "Screenshot error: " + str(e)

def image_ocr(path):
    try:
        from PIL import Image
        import pytesseract
        p = Path(path).expanduser()
        if not p.exists():
            return "Image not found"
        if settings.tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = settings.tesseract_cmd
        return pytesseract.image_to_string(Image.open(p)).strip() or "No text detected."
    except Exception as e:
        return "OCR error: " + str(e)

def screen_ocr():
    shot = take_screenshot()
    if not shot.startswith("Screenshot saved:"):
        return shot
    path = shot.replace("Screenshot saved:", "").strip()
    text = image_ocr(path)
    return f"{shot}\n\nOCR:\n{text}"

def desktop_action(action):
    if not settings.screen_control_enabled:
        return "Desktop control disabled. Set SCREEN_CONTROL_ENABLED=true in .env after review."
    action = action.lower().strip()
    if action not in SAFE_ACTIONS:
        return "Blocked. Allowed actions: " + ", ".join(SAFE_ACTIONS)
    try:
        import subprocess
        subprocess.Popen([SAFE_ACTIONS[action]], shell=False)
        return "Executed safe desktop action: " + action
    except Exception as e:
        return "Desktop action error: " + str(e)
