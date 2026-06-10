# BADSHAH-AI v2 Phase 3

Phase 3 adds:

- Better task planner
- Tool registry
- Safe app launcher
- OCR/image agent
- Project/website code generator into workspace
- Email + WhatsApp safe draft placeholders
- Improved FastAPI endpoints
- Improved Streamlit dashboard

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
ollama pull llama3.2:1b
python main.py
```

## Optional OCR

Install Tesseract OCR on Windows, then set path in `.env` if needed:

```env
TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe
```

## Run API

```bash
uvicorn badshah_ai.api.server:app --reload
```

## Run Dashboard

```bash
streamlit run badshah_ai/dashboard/app.py
```
