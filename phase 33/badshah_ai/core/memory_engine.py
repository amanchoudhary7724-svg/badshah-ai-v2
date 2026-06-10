import sqlite3
from datetime import datetime
from badshah_ai.config.settings import settings

class MemoryEngine:
    def __init__(self):
        with sqlite3.connect(settings.memory_db) as con:
            con.execute("CREATE TABLE IF NOT EXISTS memories(id INTEGER PRIMARY KEY, text TEXT, source TEXT, created_at TEXT)")

    def remember(self, text, source="chat"):
        with sqlite3.connect(settings.memory_db) as con:
            con.execute("INSERT INTO memories(text,source,created_at) VALUES(?,?,?)", (text, source, datetime.utcnow().isoformat()))
        return "Remembered."

    def recent(self, limit=10):
        with sqlite3.connect(settings.memory_db) as con:
            return con.execute("SELECT text,source,created_at FROM memories ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
