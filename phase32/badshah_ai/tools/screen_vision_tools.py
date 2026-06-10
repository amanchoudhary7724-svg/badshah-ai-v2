from badshah_ai.config.settings import settings
def screen_safety():
    return "Screen Safety: optional local screenshot/OCR only. Install optional deps first."
def take_screenshot():
    try:
        import pyautogui
        from datetime import datetime
        out = settings.safe_workspace / "screens" / f"screen_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        pyautogui.screenshot().save(out)
        return f"Screenshot saved: {out}"
    except Exception as e:
        return "Screenshot needs optional dependencies. Run installer\\INSTALL_OPTIONAL.bat. Error: " + str(e)
