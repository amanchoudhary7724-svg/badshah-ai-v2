import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel
from badshah_ai.core.brain import Brain
class BadshahWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.brain = Brain()
        self.setWindowTitle("BADSHAH-AI v3.1")
        self.resize(900, 650)
        root = QWidget(); self.setCentralWidget(root)
        layout = QVBoxLayout(root)
        layout.addWidget(QLabel("BADSHAH-AI v3.1 Integrated"))
        self.chat = QTextEdit(); self.chat.setReadOnly(True); layout.addWidget(self.chat)
        self.input = QLineEdit(); self.input.returnPressed.connect(self.send); layout.addWidget(self.input)
        btn = QPushButton("Send"); btn.clicked.connect(self.send); layout.addWidget(btn)
    def send(self):
        q = self.input.text().strip()
        if not q: return
        self.input.clear()
        self.chat.append(f"You: {q}\nBADSHAH: {self.brain.run(q)}\n")
def run_desktop():
    app = QApplication(sys.argv); w = BadshahWindow(); w.show(); sys.exit(app.exec())
