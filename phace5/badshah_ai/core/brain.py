from badshah_ai.core.memory import Memory
from badshah_ai.core.task_history import TaskHistory
from badshah_ai.core.planner import Planner
from badshah_ai.core.router import Router
from badshah_ai.models.ollama_client import OllamaClient

class Brain:
    def __init__(self):
        self.memory = Memory()
        self.tasks = TaskHistory()
        self.planner = Planner()
        self.router = Router()
        self.llm = OllamaClient()

    def run(self,q):
        try:
            agent = self.router.route(q)
            if agent:
                ans = agent.handle(q)
                tag = agent.name
            else:
                ans = self.llm.generate(self.planner.prompt(q,self.memory.recall(q)))
                tag = "chat"
            self.memory.store(q,ans,tag)
            self.tasks.add(q,tag,"success",ans[:2000])
            return ans
        except Exception as e:
            self.tasks.add(q,"error","error",str(e))
            return "Error: " + str(e)
