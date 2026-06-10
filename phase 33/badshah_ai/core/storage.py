import sqlite3
from datetime import datetime
from badshah_ai.config.settings import settings

class SQLiteStore:
    def __init__(self):
        with sqlite3.connect(settings.task_db) as con:
            con.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, query TEXT, status TEXT, result TEXT, created_at TEXT)")

    def add_task(self, query, status, result):
        with sqlite3.connect(settings.task_db) as con:
            con.execute("INSERT INTO tasks(query,status,result,created_at) VALUES(?,?,?,?)", (query, status, result, datetime.utcnow().isoformat()))
