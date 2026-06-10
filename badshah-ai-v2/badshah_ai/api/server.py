from fastapi import FastAPI
from pydantic import BaseModel
from badshah_ai.core.brain import Brain

app = FastAPI(title="BADSHAH-AI v2 API", version="0.1.0")
brain = Brain()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"name": "BADSHAH-AI v2", "status": "running"}

@app.post("/chat")
def chat(req: ChatRequest):
    return {"response": brain.run(req.message)}

@app.get("/memory/recent")
def recent_memory(limit: int = 10):
    return {"items": brain.memory.recent(limit)}
