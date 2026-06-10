import subprocess

APPS = {"notepad":"notepad.exe","calc":"calc.exe","calculator":"calc.exe","paint":"mspaint.exe"}

def open_app(name):
    k = name.lower().strip()
    if k not in APPS:
        return "Allowed apps: " + ", ".join(APPS)
    subprocess.Popen([APPS[k]], shell=False)
    return "Opened app: " + k
