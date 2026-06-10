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

    def recent(self, limit=10):
        with sqlite3.connect(self.db) as con:
            return con.execute("SELECT text,source,created_at FROM memories ORDER BY id DESC LIMIT ?", (limit,)).fetchall()

    def search(self, query, limit=5):
        words = [w for w in query.lower().split() if len(w) > 2]
        rows = []
        with sqlite3.connect(self.db) as con:
            for w in words[:5] or [query]:
                rows += con.execute("SELECT text FROM memories WHERE lower(text) LIKE ? ORDER BY id DESC LIMIT ?", (f"%{w}%", limit)).fetchall()
        return [r[0] for r in rows[:limit]]
