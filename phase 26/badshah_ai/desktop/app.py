import sys
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QLineEdit, QPushButton, QLabel, QComboBox, QSystemTrayIcon,
    QMenu, QMessageBox
)
from PyQt6.QtGui import QAction, QIcon
from badshah_ai.core.brain import Brain

STYLE = '''
QMainWindow { background: #07111f; }
QWidget { background: #07111f; color: #e5f7ff; font-family: Segoe UI; font-size: 14px; }
QTextEdit { background: #0b1729; border: 1px solid #1f6feb; border-radius: 12px; padding: 10px; color: #dff6ff; }
QLineEdit { background: #0b1729; border: 1px solid #22d3ee; border-radius: 10px; padding: 10px; color: white; }
QPushButton { background: #0ea5e9; color: white; border: 0; border-radius: 10px; padding: 10px 14px; font-weight: bold; }
QPushButton:hover { background: #38bdf8; }
QComboBox { background: #0b1729; border: 1px solid #22d3ee; border-radius: 8px; padding: 6px; color: white; }
QLabel#title { font-size: 26px; font-weight: bold; color: #22d3ee; }
'''

class Worker(QThread):
    done = pyqtSignal(str)
    def __init__(self, brain, command):
        super().__init__()
        self.brain = brain
        self.command = command
    def run(self):
        self.done.emit(self.brain.run(self.command))

class BadshahWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.brain = Brain()
        self.setWindowTitle("BADSHAH-AI v2.6")
        self.resize(980, 680)
        self.setStyleSheet(STYLE)
        self.worker = None
        self._build_ui()
        self._build_tray()

    def _build_ui(self):
        root = QWidget()
        self.setCentralWidget(root)
        layout = QVBoxLayout(root)

        title = QLabel("BADSHAH-AI  •  Desktop Command Center")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)
        self.chat.setText("BADSHAH-AI ready. Type a command below.\n")
        layout.addWidget(self.chat)

        row = QHBoxLayout()
        self.role = QComboBox()
        self.role.addItems(["default", "fast", "coding", "smart"])
        self.input = QLineEdit()
        self.input.setPlaceholderText("Ask anything... e.g. create website portfolio")
        self.input.returnPressed.connect(self.send)
        send_btn = QPushButton("Send")
        send_btn.clicked.connect(self.send)
        row.addWidget(self.role)
        row.addWidget(self.input, 1)
        row.addWidget(send_btn)
        layout.addLayout(row)

        tools = QHBoxLayout()
        for label, cmd in [
            ("Help", "help"),
            ("Models", "models"),
            ("Health", "model health"),
            ("Create Website", "create website portfolio"),
            ("Plugins", "plugins"),
        ]:
            b = QPushButton(label)
            b.clicked.connect(lambda _, c=cmd: self.run_command(c))
            tools.addWidget(b)
        layout.addLayout(tools)

    def _build_tray(self):
        try:
            self.tray = QSystemTrayIcon(self)
            menu = QMenu()
            show_action = QAction("Show BADSHAH-AI", self)
            quit_action = QAction("Quit", self)
            show_action.triggered.connect(self.show)
            quit_action.triggered.connect(QApplication.quit)
            menu.addAction(show_action)
            menu.addAction(quit_action)
            self.tray.setContextMenu(menu)
            self.tray.setToolTip("BADSHAH-AI")
            self.tray.show()
        except Exception:
            self.tray = None

    def append(self, who, text):
        self.chat.append(f"\n{who}:\n{text}\n")

    def send(self):
        text = self.input.text().strip()
        if not text:
            return
        role = self.role.currentText()
        command = f"ask {role} {text}" if role != "default" and not text.startswith("ask ") else text
        self.input.clear()
        self.run_command(command)

    def run_command(self, command):
        self.append("You", command)
        self.worker = Worker(self.brain, command)
        self.worker.done.connect(lambda out: self.append("BADSHAH", out))
        self.worker.start()

def run_desktop():
    app = QApplication(sys.argv)
    w = BadshahWindow()
    w.show()
    sys.exit(app.exec())
