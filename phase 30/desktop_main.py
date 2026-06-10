try:
    from badshah_ai.desktop.app import run_desktop
    run_desktop()
except Exception as e:
    print("Desktop UI error:", e)
    print("Install PyQt6 or use main.py CLI.")
