import sqlite3
from datetime import datetime
from badshah_ai.config.settings import settings

class SQLiteStore:
    def __init__(self):
        self.memory_db = settings.memory_db
        self.task_db = settings.task_db
        self._init()

    def _init(self):
        with sqlite3.connect(self.memory_db) as con:
            con.execute("CREATE TABLE IF NOT EXISTS memories(id INTEGER PRIMARY KEY, query TEXT, response TEXT, created_at TEXT)")
        with sqlite3.connect(self.task_db) as con:
            con.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, query TEXT, status TEXT, result TEXT, created_at TEXT)")

    def add_memory(self, query, response):
        with sqlite3.connect(self.memory_db) as con:
            con.execute("INSERT INTO memories(query,response,created_at) VALUES(?,?,?)", (query, response, datetime.utcnow().isoformat()))

    def recent_memory(self, limit=10):
        with sqlite3.connect(self.memory_db) as con:
            return con.execute("SELECT query,response,created_at FROM memories ORDER BY id DESC LIMIT ?", (limit,)).fetchall()

    def add_task(self, query, status, result):
        with sqlite3.connect(self.task_db) as con:
            con.execute("INSERT INTO tasks(query,status,result,created_at) VALUES(?,?,?,?)", (query, status, result, datetime.utcnow().isoformat()))

    def recent_tasks(self, limit=10):
        with sqlite3.connect(self.task_db) as con:
            return con.execute("SELECT query,status,result,created_at FROM tasks ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
