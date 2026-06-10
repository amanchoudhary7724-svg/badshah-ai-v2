import sqlite3
from datetime import datetime
from badshah_ai.config.settings import settings

class Memory:
    def __init__(self):
        self.db = settings.memory_db
        self.db.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(self.db) as con:
            con.execute("CREATE TABLE IF NOT EXISTS memories(id INTEGER PRIMARY KEY, query TEXT, response TEXT, tag TEXT, created_at TEXT)")

    def store(self, query, response, tag="chat"):
        with sqlite3.connect(self.db) as con:
            con.execute(
                "INSERT INTO memories(query,response,tag,created_at) VALUES(?,?,?,?)",
                (query,response,tag,datetime.utcnow().isoformat()),
            )

    def recall(self, query, limit=5):
        word = (query.split() or [""])[0]
        with sqlite3.connect(self.db) as con:
            rows = con.execute(
                "SELECT query,response FROM memories WHERE query LIKE ? OR response LIKE ? ORDER BY id DESC LIMIT ?",
                (f"%{word}%",f"%{word}%",limit),
            ).fetchall()
        return "\n".join([f"User:{q}\nAssistant:{r}" for q,r in rows])

    def recent(self, limit=10):
        with sqlite3.connect(self.db) as con:
            rows = con.execute("SELECT query,response,tag,created_at FROM memories ORDER BY id DESC LIMIT ?",(limit,)).fetchall()
        return [{"query":q,"response":r,"tag":t,"created_at":c} for q,r,t,c in rows]
