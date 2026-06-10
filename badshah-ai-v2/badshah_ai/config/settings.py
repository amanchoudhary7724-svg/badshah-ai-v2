from pathlib import Path
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseModel):
    app_name: str = Field(default=os.getenv("APP_NAME", "BADSHAH-AI"))
    ollama_url: str = Field(default=os.getenv("OLLAMA_URL", "http://localhost:11434"))
    default_model: str = Field(default=os.getenv("DEFAULT_MODEL", "llama3.2:1b"))
    memory_db: Path = Field(default=BASE_DIR / os.getenv("MEMORY_DB", "data/memory/badshah_memory.sqlite3"))
    safe_workspace: Path = Field(default=BASE_DIR / os.getenv("SAFE_WORKSPACE", "workspace"))
    log_file: Path = Field(default=BASE_DIR / os.getenv("LOG_FILE", "logs/badshah.log"))

    def prepare_dirs(self) -> None:
        self.memory_db.parent.mkdir(parents=True, exist_ok=True)
        self.safe_workspace.mkdir(parents=True, exist_ok=True)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

settings = Settings()
settings.prepare_dirs()
