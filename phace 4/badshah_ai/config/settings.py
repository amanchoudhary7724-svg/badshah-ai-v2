from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
BASE_DIR = Path(__file__).resolve().parents[2]

def bool_env(name, default=False):
    v=os.getenv(name)
    return default if v is None else v.lower() in {"1","true","yes","on"}

class Settings:
    app_name=os.getenv("APP_NAME","BADSHAH-AI")
    ollama_url=os.getenv("OLLAMA_URL","http://localhost:11434")
    default_model=os.getenv("DEFAULT_MODEL","llama3.2:1b")
    memory_db=BASE_DIR / os.getenv("MEMORY_DB","data/memory/badshah_memory.sqlite3")
    task_db=BASE_DIR / os.getenv("TASK_DB","data/memory/badshah_tasks.sqlite3")
    chroma_dir=BASE_DIR / os.getenv("CHROMA_DIR","data/memory/chroma")
    safe_workspace=BASE_DIR / os.getenv("SAFE_WORKSPACE","workspace")
    export_dir=BASE_DIR / os.getenv("EXPORT_DIR","exports")
    log_file=BASE_DIR / os.getenv("LOG_FILE","logs/badshah.log")
    enable_chroma=bool_env("ENABLE_CHROMA", False)
    tesseract_cmd=os.getenv("TESSERACT_CMD","")
    voice_enabled=bool_env("VOICE_ENABLED", False)

    def prepare_dirs(self):
        for p in [self.memory_db.parent,self.task_db.parent,self.chroma_dir,self.safe_workspace,self.export_dir,self.log_file.parent]:
            p.mkdir(parents=True, exist_ok=True)

settings=Settings()
settings.prepare_dirs()
