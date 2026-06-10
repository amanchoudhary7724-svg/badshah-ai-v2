try:
    from badshah_ai.desktop.app import run_desktop
    run_desktop()
except Exception as e:
    print("Desktop UI optional dependency error:", e)
    print("Run: installer\\INSTALL_OPTIONAL.bat")
