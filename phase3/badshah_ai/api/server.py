from fastapi import FastAPI
from pydantic import BaseModel
from badshah_ai.core.brain import Brain
from badshah_ai.tools.pdf_tools import extract_pdf_text
from badshah_ai.tools.excel_tools import summarize_table
from badshah_ai.tools.ocr_tools import extract_image_text
from badshah_ai.tools.project_tools import create_static_website

app = FastAPI(title="BADSHAH-AI v2 API", version="0.3.0")
brain = Brain()

class ChatRequest(BaseModel):
    message: str

class PathRequest(BaseModel):
    path: str

class ProjectRequest(BaseModel):
    name: str = "badshah_site"

@app.get("/")
def root():
    return {"name": "BADSHAH-AI v2", "version": "0.3.0", "status": "running"}

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

@app.post("/tools/ocr")
def ocr(req: PathRequest):
    return {"text": extract_image_text(req.path)}

@app.post("/tools/project/static-website")
def static_website(req: ProjectRequest):
    return {"result": create_static_website(req.name)}
