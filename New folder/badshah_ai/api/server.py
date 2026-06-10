from fastapi import FastAPI
from pydantic import BaseModel
from badshah_ai.core.brain import Brain
from badshah_ai.tools.pdf_tools import extract_pdf_text
from badshah_ai.tools.excel_tools import summarize_table

app = FastAPI(title="BADSHAH-AI v2 API", version="0.2.0")
brain = Brain()

class ChatRequest(BaseModel):
    message: str

class PathRequest(BaseModel):
    path: str

@app.get("/")
def root():
    return {"name": "BADSHAH-AI v2", "version": "0.2.0", "status": "running"}

@app.post("/chat")
def chat(req: ChatRequest):
    return {"response": brain.run(req.message)}

@app.get("/memory/recent")
def recent_memory(limit: int = 10):
    return {"items": brain.memory.recent(limit)}

@app.post("/tools/pdf/extract")
def pdf_extract(req: PathRequest):
    return {"text": extract_pdf_text(req.path)}

@app.post("/tools/excel/summary")
def excel_summary(req: PathRequest):
    return {"summary": summarize_table(req.path)}
