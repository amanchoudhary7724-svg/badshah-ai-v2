# BADSHAH-AI v2 Phase 1

Runnable foundation for a local AI assistant.

## Features
- CLI chat
- FastAPI `/chat` endpoint
- Ollama integration
- SQLite long-term memory
- Agent router
- Coding, Excel, PDF, Browser, Vision agent placeholders

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

Open:

```text
http://127.0.0.1:8000/docs
```

## Push to GitHub

```bash
git add .
git commit -m "Add BADSHAH-AI v2 phase 1 core"
git push origin main
```
