from __future__ import annotations
import logging
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from badshah_ai.config.settings import settings

logger = logging.getLogger(__name__)

class Memory:
    def __init__(self, db_path: Path | None = None) -> None:
        self.db_path = db_path or settings.memory_db
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()
        self.chroma_collection = None
        if settings.enable_chroma:
            self._init_chroma()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def _init_db(self) -> None:
        with self._connect() as con:
            con.execute(
                '''
                CREATE TABLE IF NOT EXISTS memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    query TEXT NOT NULL,
                    response TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    tag TEXT DEFAULT 'chat'
                )
                '''
            )
            con.execute("CREATE INDEX IF NOT EXISTS idx_memories_created_at ON memories(created_at)")

    def _init_chroma(self) -> None:
        try:
            import chromadb
            client = chromadb.PersistentClient(path=str(settings.chroma_dir))
            self.chroma_collection = client.get_or_create_collection("badshah_memory")
        except Exception:
            logger.exception("ChromaDB init failed; falling back to SQLite only")
            self.chroma_collection = None

    def store(self, query: str, response: str, tag: str = "chat") -> None:
        now = datetime.now(timezone.utc).isoformat()
        with self._connect() as con:
            cur = con.execute(
                "INSERT INTO memories(query, response, created_at, tag) VALUES (?, ?, ?, ?)",
                (query, response, now, tag),
            )
            memory_id = cur.lastrowid

        if self.chroma_collection is not None:
            try:
                self.chroma_collection.add(
                    ids=[str(memory_id)],
                    documents=[f"User: {query}\nAssistant: {response}"],
                    metadatas=[{"created_at": now, "tag": tag}],
                )
            except Exception:
                logger.exception("ChromaDB store failed")

    def recall(self, query: str, limit: int = 5) -> str:
        chroma_result = self._recall_chroma(query, limit)
        if chroma_result:
            return chroma_result
        return self._recall_sqlite(query, limit)

    def _recall_chroma(self, query: str, limit: int) -> str:
        if self.chroma_collection is None:
            return ""
        try:
            result = self.chroma_collection.query(query_texts=[query], n_results=limit)
            docs = result.get("documents", [[]])[0]
            return "\n\n".join(docs)
        except Exception:
            logger.exception("ChromaDB recall failed")
            return ""

    def _recall_sqlite(self, query: str, limit: int) -> str:
        keywords = [w for w in query.lower().split() if len(w) > 3]
        if not keywords:
            return ""

        rows = []
        with self._connect() as con:
            for kw in keywords[:5]:
                rows.extend(
                    con.execute(
                        "SELECT query, response, created_at FROM memories WHERE lower(query) LIKE ? OR lower(response) LIKE ? ORDER BY id DESC LIMIT ?",
                        (f"%{kw}%", f"%{kw}%", limit),
                    ).fetchall()
                )

        unique = []
        seen = set()
        for q, r, t in rows:
            key = (q, r)
            if key not in seen:
                seen.add(key)
                unique.append(f"[{t}] User: {q}\nAssistant: {r}")
            if len(unique) >= limit:
                break
        return "\n\n".join(unique)

    def recent(self, limit: int = 10) -> list[dict]:
        with self._connect() as con:
            rows = con.execute(
                "SELECT query, response, created_at, tag FROM memories ORDER BY id DESC LIMIT ?",
                (limit,),
            ).fetchall()
        return [{"query": q, "response": r, "created_at": t, "tag": tag} for q, r, t, tag in rows]
