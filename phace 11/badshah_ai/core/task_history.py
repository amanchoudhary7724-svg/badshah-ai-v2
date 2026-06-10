import sqlite3
from datetime import datetime
from badshah_ai.config.settings import settings

class TaskHistory:
    def __init__(self):
        self.db = settings.task_db
        with sqlite3.connect(self.db) as con:
            con.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, query TEXT, agent TEXT, status TEXT, result TEXT, created_at TEXT)")

    def add(self, query, agent, status, result):
        with sqlite3.connect(self.db) as con:
            con.execute("INSERT INTO tasks(query,agent,status,result,created_at) VALUES(?,?,?,?,?)", (query, agent, status, result, datetime.utcnow().isoformat()))
