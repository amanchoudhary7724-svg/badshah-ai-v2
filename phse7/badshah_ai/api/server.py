from fastapi import FastAPI
from pydantic import BaseModel
from badshah_ai.core.brain import Brain
from badshah_ai.tools.export_tools import export_workspace, backup_workspace
from badshah_ai.tools.health_tools import health_check, diagnostics
from badshah_ai.tools.selfmod_tools import propose_self_modification, list_patches, apply_latest_patch
from badshah_ai.plugins.manifest import list_plugins

app = FastAPI(title="BADSHAH-AI v2", version="0.7.0")
brain = Brain()

class ChatRequest(BaseModel):
    message: str

class SelfModRequest(BaseModel):
    request: str

@app.get("/")
def root():
    return {"status":"running","version":"0.7.0"}

@app.get("/health")
def health():
    return {"result": health_check()}

@app.get("/diagnostics")
def diag():
    return {"result": diagnostics()}

@app.get("/plugins")
def plugins():
    return {"items": list_plugins()}

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

@app.post("/backup/workspace")
def backup():
    return {"result": backup_workspace()}

@app.post("/selfmod/propose")
def selfmod(req: SelfModRequest):
    return {"result": propose_self_modification(req.request)}

@app.post("/selfmod/apply-latest")
def apply_patch():
    return {"result": apply_latest_patch()}

@app.get("/selfmod/patches")
def patches():
    return {"result": list_patches()}
