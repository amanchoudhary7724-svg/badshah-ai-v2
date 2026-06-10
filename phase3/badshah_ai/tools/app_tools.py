import subprocess
import sys

ALLOWED_APPS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "calc": "calc.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
}

def open_app(app_name: str) -> str:
    key = app_name.lower().strip()
    if key not in ALLOWED_APPS:
        return "App blocked or not whitelisted. Allowed: " + ", ".join(sorted(ALLOWED_APPS))
    try:
        subprocess.Popen([ALLOWED_APPS[key]], shell=False)
        return f"Opened app: {key}"
    except Exception as exc:
        return f"Could not open app: {exc}"
