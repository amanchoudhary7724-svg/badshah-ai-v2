# BADSHAH-AI v2 Phase 4 Fast

Adds:
- Workspace ZIP export
- Task history
- Voice TTS starter
- Browser scrape starter
- Dashboard/API upgrades

## Run

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
ollama pull llama3.2:1b
python main.py
```

API:
```bash
uvicorn badshah_ai.api.server:app --reload
```

Dashboard:
```bash
streamlit run badshah_ai/dashboard/app.py
```

Push:
```bash
git add .
git commit -m "Add BADSHAH-AI v2 phase 4"
git push origin main
```
