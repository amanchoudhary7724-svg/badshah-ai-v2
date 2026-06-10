import sqlite3
from datetime import datetime
from badshah_ai.config.settings import settings
class MemoryEngine:
    def __init__(self):
        self.db = settings.memory_db
        self.chroma = None
        self._init_sqlite()
        if settings.enable_chroma:
            self._init_chroma()
    def _init_sqlite(self):
        with sqlite3.connect(self.db) as con:
            con.execute("CREATE TABLE IF NOT EXISTS memories(id INTEGER PRIMARY KEY, text TEXT, source TEXT, created_at TEXT)")
    def _init_chroma(self):
        try:
            import chromadb
            client = chromadb.PersistentClient(path=str(settings.chroma_dir))
            self.chroma = client.get_or_create_collection("badshah_memory")
        except Exception:
            self.chroma = None
    def remember(self, text, source="user"):
        now = datetime.utcnow().isoformat()
        with sqlite3.connect(self.db) as con:
            cur = con.execute("INSERT INTO memories(text,source,created_at) VALUES(?,?,?)", (text, source, now))
            mid = cur.lastrowid
        if self.chroma:
            try: self.chroma.add(ids=[str(mid)], documents=[text], metadatas=[{"source": source, "created_at": now}])
            except Exception: pass
        return f"Remembered: {text}"
    def recent(self, limit=10):
        with sqlite3.connect(self.db) as con:
            return con.execute("SELECT text,source,created_at FROM memories ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
    def search(self, query, limit=5):
        if self.chroma:
            try:
                docs = self.chroma.query(query_texts=[query], n_results=limit).get("documents", [[]])[0]
                if docs: return docs
            except Exception: pass
        words = [w for w in query.lower().split() if len(w) > 2]
        rows = []
        with sqlite3.connect(self.db) as con:
            for w in words[:5] or [query]:
                rows += con.execute("SELECT text FROM memories WHERE lower(text) LIKE ? ORDER BY id DESC LIMIT ?", (f"%{w}%", limit)).fetchall()
        out, seen = [], set()
        for (text,) in rows:
            if text not in seen:
                seen.add(text); out.append(text)
            if len(out) >= limit: break
        return out
    def clear(self):
        with sqlite3.connect(self.db) as con:
            con.execute("DELETE FROM memories")
        return "Memory cleared."
