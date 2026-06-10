import sqlite3
from datetime import datetime
from badshah_ai.config.settings import settings
class MemoryEngine:
    def __init__(self):
        self.db = settings.memory_db
        with sqlite3.connect(self.db) as con:
            con.execute("CREATE TABLE IF NOT EXISTS memories(id INTEGER PRIMARY KEY, text TEXT, source TEXT, created_at TEXT)")
    def remember(self, text, source="chat"):
        with sqlite3.connect(self.db) as con:
            con.execute("INSERT INTO memories(text,source,created_at) VALUES(?,?,?)", (text, source, datetime.utcnow().isoformat()))
        return "Remembered."
