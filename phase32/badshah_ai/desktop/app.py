def run_desktop():
    try:
        from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit
        import sys
        app = QApplication(sys.argv)
        w = QMainWindow()
        w.setWindowTitle("BADSHAH-AI v3.2")
        box = QTextEdit()
        box.setText("BADSHAH-AI Desktop optional UI. Use CLI for full commands.")
        w.setCentralWidget(box)
        w.resize(800, 500)
        w.show()
        sys.exit(app.exec())
    except Exception as e:
        print("PyQt6 missing. Run installer\\INSTALL_OPTIONAL.bat. Error:", e)
