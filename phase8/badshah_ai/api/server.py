from fastapi import FastAPI
from pydantic import BaseModel
from badshah_ai.core.brain import Brain
from badshah_ai.plugins.manifest import list_plugins

app = FastAPI(title="BADSHAH-AI v2", version="0.8.0")
brain = Brain()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status":"running","version":"0.8.0"}

@app.post("/chat")
def chat(req: ChatRequest):
    return {"response": brain.run(req.message)}

@app.get("/plugins")
def plugins():
    return {"items": list_plugins()}

@app.get("/memory/recent")
def memory(limit:int=10):
    return {"items": brain.memory.recent(limit)}

@app.get("/tasks/recent")
def tasks(limit:int=20):
    return {"items": brain.tasks.recent(limit)}
