from __future__ import annotations
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from badshah_ai.config.settings import settings

class Memory:
    def __init__(self, db_path: Path | None = None) -> None:
        self.db_path = db_path or settings.memory_db
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

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
                    created_at TEXT NOT NULL
                )
                '''
            )
            con.execute("CREATE INDEX IF NOT EXISTS idx_memories_created_at ON memories(created_at)")

    def store(self, query: str, response: str) -> None:
        now = datetime.now(timezone.utc).isoformat()
        with self._connect() as con:
            con.execute(
                "INSERT INTO memories(query, response, created_at) VALUES (?, ?, ?)",
                (query, response, now),
            )

    def recall(self, query: str, limit: int = 5) -> str:
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
                "SELECT query, response, created_at FROM memories ORDER BY id DESC LIMIT ?",
                (limit,),
            ).fetchall()
        return [{"query": q, "response": r, "created_at": t} for q, r, t in rows]
