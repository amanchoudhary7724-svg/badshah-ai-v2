try:
    from badshah_ai.desktop.app import run_desktop
    run_desktop()
except Exception as e:
    print("Desktop UI error:", e)
    print("Use CLI: python main.py")
