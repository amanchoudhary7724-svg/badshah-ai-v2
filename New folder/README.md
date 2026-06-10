# BADSHAH-AI v2 Phase 2

Phase 2 adds practical local tools:

- SQLite memory + optional ChromaDB semantic memory
- PDF text extraction
- Excel/CSV summary
- Safe browser open/search
- Safe workspace file writer/reader
- FastAPI endpoints for chat, tools, memory
- Streamlit dashboard starter

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
ollama pull llama3.2:1b
python main.py
```

## API

```bash
uvicorn badshah_ai.api.server:app --reload
```

## Dashboard

```bash
streamlit run badshah_ai/dashboard/app.py
```

## Important

Files are only written inside `workspace/` for safety.
