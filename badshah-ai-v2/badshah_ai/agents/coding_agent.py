from badshah_ai.agents.base import BaseAgent
from badshah_ai.models.ollama_client import OllamaClient

class CodingAgent(BaseAgent):
    name = "coding"

    def __init__(self) -> None:
        self.llm = OllamaClient()

    def handle(self, query: str) -> str:
        prompt = (
            "You are BADSHAH Coding Agent. Generate clean, runnable, secure code. "
            "Include file names and run commands when useful. User request:\n" + query
        )
        return self.llm.generate(prompt)
