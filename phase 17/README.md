# BADSHAH-AI v2 — v1.7 Advanced Memory

Phase-17 adds advanced memory:

- `remember ...`
- `memory`
- `memory search ...`
- `forget memory` safe clear command
- SQLite memory always enabled
- Optional ChromaDB semantic memory
- Dashboard memory tab

## Install

```bat
scripts\setup_windows.bat
```

## Enable ChromaDB

In `.env`:

```env
ENABLE_CHROMA=true
```

## Commands

```text
remember my name is Sourabh
memory
memory search Sourabh
forget memory
```

## Push

```bash
git add .
git commit -m "Add BADSHAH-AI v2 v1.7 advanced memory"
git push origin main
```
