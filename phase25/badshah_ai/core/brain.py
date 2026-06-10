import json, badshah_ai
from badshah_ai.models.llm_router import LLMRouter
from badshah_ai.core.storage import SQLiteStore
from badshah_ai.core.memory_engine import MemoryEngine
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.agents.agent_registry import list_agents

HELP = '''Commands:
help
version
agents
plugins
models
model health
model use fast
model use coding
model use smart
ask fast hello
ask coding write python function
ask smart explain AI agents
'''

class Brain:
    def __init__(self):
        self.router = LLMRouter()
        self.tasks = SQLiteStore()
        self.memory = MemoryEngine()

    def run(self, q: str) -> str:
        x = q.lower().strip()
        try:
            if x == "help": ans = HELP
            elif x == "version": ans = f"BADSHAH-AI v{badshah_ai.__version__}"
            elif x == "plugins": ans = json.dumps(list_plugins(), indent=2)
            elif x == "agents": ans = json.dumps(list_agents(), indent=2)
            elif x == "models": ans = self.router.list_models_config()
            elif x == "model health": ans = self.router.health()
            elif x.startswith("model use "):
                role = x.split(" ", 2)[2]
                if role in self.router.role_models:
                    self.router.active_role = role
                    ans = f"Active model role set to {role}: {self.router.role_models[role]}"
                else:
                    ans = "Available roles: " + ", ".join(self.router.role_models)
            elif x.startswith("ask "):
                parts = q.split(" ", 2)
                if len(parts) < 3:
                    ans = "Usage: ask coding your question"
                else:
                    role, prompt = parts[1], parts[2]
                    ans = self.router.generate(prompt, role=role)
            else:
                ans = self.router.generate(q, role=self.router.active_role)
            self.memory.remember(f"User: {q}\nAssistant: {ans}")
            self.tasks.add_task(q, "success", ans[:1000])
            return ans
        except Exception as e:
            self.tasks.add_task(q, "error", str(e))
            return "Error: " + str(e)
