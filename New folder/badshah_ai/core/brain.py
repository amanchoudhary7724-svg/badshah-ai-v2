import logging
from badshah_ai.core.memory import Memory
from badshah_ai.core.planner import Planner
from badshah_ai.core.router import Router
from badshah_ai.models.ollama_client import OllamaClient

logger = logging.getLogger(__name__)

class Brain:
    def __init__(self) -> None:
        self.memory = Memory()
        self.planner = Planner()
        self.router = Router()
        self.llm = OllamaClient()

    def run(self, query: str) -> str:
        try:
            agent = self.router.route(query)
            if agent is not None and agent.can_handle(query):
                response = agent.handle(query)
            else:
                context = self.memory.recall(query)
                prompt = self.planner.create_prompt(query, context)
                response = self.llm.generate(prompt)

            self.memory.store(query, response)
            return response
        except Exception as exc:
            logger.exception("Brain failed")
            return f"Error: {exc}"
