import subprocess
ALLOWED = {"notepad":"notepad.exe", "calc":"calc.exe", "calculator":"calc.exe", "paint":"mspaint.exe"}
def open_app(name):
    key = name.lower().strip()
    if key not in ALLOWED: return "Allowed apps: " + ", ".join(ALLOWED)
    subprocess.Popen([ALLOWED[key]], shell=False)
    return "Opened app: " + key
