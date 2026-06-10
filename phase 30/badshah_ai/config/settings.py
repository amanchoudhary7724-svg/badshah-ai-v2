from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
BASE_DIR = Path(__file__).resolve().parents[2]

class Settings:
    def __init__(self):
        self.app_name = os.getenv("APP_NAME", "BADSHAH-AI")
        self.ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434")
        self.default_model = os.getenv("DEFAULT_MODEL", "llama3.2:1b")
        self.memory_db = BASE_DIR / os.getenv("MEMORY_DB", "data/memory/badshah_memory.sqlite3")
        self.task_db = BASE_DIR / os.getenv("TASK_DB", "data/memory/badshah_tasks.sqlite3")
        self.safe_workspace = BASE_DIR / os.getenv("SAFE_WORKSPACE", "workspace")
        self.export_dir = BASE_DIR / os.getenv("EXPORT_DIR", "exports")
        self.log_file = BASE_DIR / os.getenv("LOG_FILE", "logs/badshah.log")
        self.prepare_dirs()
    def prepare_dirs(self):
        for p in [self.memory_db.parent, self.task_db.parent, self.safe_workspace, self.export_dir, self.log_file.parent]:
            p.mkdir(parents=True, exist_ok=True)
settings = Settings()
