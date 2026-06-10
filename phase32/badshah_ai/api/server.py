from fastapi import FastAPI
from pydantic import BaseModel
from badshah_ai.core.brain import Brain
app = FastAPI(title="BADSHAH-AI", version="3.2.0")
brain = Brain()
class ChatRequest(BaseModel): message: str
@app.get("/")
def root(): return {"status": "running", "version": "3.2.0"}
@app.post("/chat")
def chat(req: ChatRequest): return {"response": brain.run(req.message)}
