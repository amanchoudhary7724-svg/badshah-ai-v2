from fastapi import FastAPI
from pydantic import BaseModel
from badshah_ai.core.brain import Brain
from badshah_ai.tools.export_tools import export_workspace
from badshah_ai.tools.health_tools import health_check
from badshah_ai.tools.selfmod_tools import propose_self_modification, list_patches

app = FastAPI(title="BADSHAH-AI v2", version="0.5.0")
brain = Brain()

class ChatRequest(BaseModel):
    message: str

class SelfModRequest(BaseModel):
    request: str

@app.get("/")
def root():
    return {"status":"running","version":"0.5.0"}

@app.get("/health")
def health():
    return {"result": health_check()}

@app.post("/chat")
def chat(req: ChatRequest):
    return {"response": brain.run(req.message)}

@app.get("/memory/recent")
def memory(limit:int=10):
    return {"items": brain.memory.recent(limit)}

@app.get("/tasks/recent")
def tasks(limit:int=20):
    return {"items": brain.tasks.recent(limit)}

@app.post("/export/workspace")
def export():
    return {"result": export_workspace()}

@app.post("/selfmod/propose")
def selfmod(req: SelfModRequest):
    return {"result": propose_self_modification(req.request)}

@app.get("/selfmod/patches")
def patches():
    return {"result": list_patches()}
