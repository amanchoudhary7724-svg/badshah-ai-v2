from fastapi import FastAPI
from pydantic import BaseModel
from badshah_ai.core.brain import Brain
from badshah_ai.plugins.manifest import list_plugins
app = FastAPI(title="BADSHAH-AI", version="3.1.0")
brain = Brain()
class ChatRequest(BaseModel): message: str
@app.get("/")
def root(): return {"status": "running", "version": "3.1.0"}
@app.post("/chat")
def chat(req: ChatRequest): return {"response": brain.run(req.message)}
@app.get("/plugins")
def plugins(): return {"items": list_plugins(), "marketplace": brain.plugins.available()}
