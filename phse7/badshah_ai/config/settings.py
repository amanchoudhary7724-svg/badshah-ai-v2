from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
BASE_DIR = Path(__file__).resolve().parents[2]

def bool_env(name, default=False):
    v = os.getenv(name)
    return default if v is None else v.lower() in {"1","true","yes","on"}

class Settings:
    app_name = os.getenv("APP_NAME","BADSHAH-AI")
    ollama_url = os.getenv("OLLAMA_URL","http://localhost:11434")
    default_model = os.getenv("DEFAULT_MODEL","llama3.2:1b")
    memory_db = BASE_DIR / os.getenv("MEMORY_DB","data/memory/badshah_memory.sqlite3")
    task_db = BASE_DIR / os.getenv("TASK_DB","data/memory/badshah_tasks.sqlite3")
    safe_workspace = BASE_DIR / os.getenv("SAFE_WORKSPACE","workspace")
    export_dir = BASE_DIR / os.getenv("EXPORT_DIR","exports")
    log_file = BASE_DIR / os.getenv("LOG_FILE","logs/badshah.log")
    voice_enabled = bool_env("VOICE_ENABLED", False)
    tesseract_cmd = os.getenv("TESSERACT_CMD","")

    def prepare_dirs(self):
        for p in [self.memory_db.parent,self.task_db.parent,self.safe_workspace,self.export_dir,self.log_file.parent]:
            p.mkdir(parents=True, exist_ok=True)

    def as_dict(self):
        return {
            "app_name": self.app_name,
            "ollama_url": self.ollama_url,
            "default_model": self.default_model,
            "memory_db": str(self.memory_db),
            "task_db": str(self.task_db),
            "safe_workspace": str(self.safe_workspace),
            "export_dir": str(self.export_dir),
            "log_file": str(self.log_file),
            "voice_enabled": self.voice_enabled,
            "tesseract_cmd_set": bool(self.tesseract_cmd),
        }

settings = Settings()
settings.prepare_dirs()
