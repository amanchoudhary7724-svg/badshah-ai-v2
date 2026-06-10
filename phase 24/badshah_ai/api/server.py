from fastapi import FastAPI
from pydantic import BaseModel
from badshah_ai.core.brain import Brain
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.agents.agent_registry import list_agents
app = FastAPI(title="BADSHAH-AI", version="2.4.0")
brain = Brain()
class ChatRequest(BaseModel): message: str
@app.get("/")
def root(): return {"status": "running", "version": "2.4.0"}
@app.post("/chat")
def chat(req: ChatRequest): return {"response": brain.run(req.message)}
@app.get("/plugins")
def plugins(): return {"items": list_plugins()}
@app.get("/agents")
def agents(): return {"items": list_agents()}
