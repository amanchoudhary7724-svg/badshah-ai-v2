import sqlite3
from datetime import datetime
from badshah_ai.config.settings import settings

class TaskHistory:
    def __init__(self):
        self.db = settings.task_db
        self.db.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(self.db) as con:
            con.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, query TEXT, agent TEXT, status TEXT, result TEXT, created_at TEXT)")

    def add(self, query, agent, status, result):
        with sqlite3.connect(self.db) as con:
            con.execute("INSERT INTO tasks(query,agent,status,result,created_at) VALUES(?,?,?,?,?)", (query,agent,status,result,datetime.utcnow().isoformat()))

    def recent(self, limit=20):
        with sqlite3.connect(self.db) as con:
            rows = con.execute("SELECT query,agent,status,result,created_at FROM tasks ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
        return [{"query":q,"agent":a,"status":s,"result":r,"created_at":c} for q,a,s,r,c in rows]
