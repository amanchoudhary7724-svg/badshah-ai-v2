from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
BASE_DIR = Path(__file__).resolve().parents[2]

def bool_env(name, default=False):
    v = os.getenv(name)
    return default if v is None else v.lower() in {"1","true","yes","on"}

class Settings:
    def __init__(self):
        self.app_name = os.getenv("APP_NAME", "BADSHAH-AI")
        self.ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434")
        self.default_model = os.getenv("DEFAULT_MODEL", "llama3.2:1b")
        self.memory_db = BASE_DIR / os.getenv("MEMORY_DB", "data/memory/badshah_memory.sqlite3")
        self.task_db = BASE_DIR / os.getenv("TASK_DB", "data/memory/badshah_tasks.sqlite3")
        self.chroma_dir = BASE_DIR / os.getenv("CHROMA_DIR", "data/memory/chroma")
        self.enable_chroma = bool_env("ENABLE_CHROMA", False)
        self.safe_workspace = BASE_DIR / os.getenv("SAFE_WORKSPACE", "workspace")
        self.export_dir = BASE_DIR / os.getenv("EXPORT_DIR", "exports")
        self.log_file = BASE_DIR / os.getenv("LOG_FILE", "logs/badshah.log")
        self.tesseract_cmd = os.getenv("TESSERACT_CMD", "")
        self.browser_headless = bool_env("BROWSER_HEADLESS", True)
        self.allow_destructive_actions = bool_env("ALLOW_DESTRUCTIVE_ACTIONS", False)
        self.prepare_dirs()
    def prepare_dirs(self):
        for p in [self.memory_db.parent, self.task_db.parent, self.chroma_dir, self.safe_workspace, self.export_dir, self.log_file.parent]:
            p.mkdir(parents=True, exist_ok=True)
settings = Settings()
