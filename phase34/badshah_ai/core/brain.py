import json
import badshah_ai
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.core.storage import SQLiteStore
from badshah_ai.core.memory_engine import MemoryEngine
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.agents.agent_registry import list_agents
from badshah_ai.tools.doctor import doctor_report
from badshah_ai.tools.migration_tools import repo_validate, migration_guide, migration_checklist

HELP = '''BADSHAH-AI v3.4 Commands:
doctor
version
migration guide
migration checklist
repo validate
agents
plugins
health check
help
'''

class Brain:
    def __init__(self):
        self.llm = OllamaClient()
        self.tasks = SQLiteStore()
        self.memory = MemoryEngine()

    def run(self, q):
        x = q.lower().strip()
        try:
            if x == "help": ans = HELP
            elif x == "doctor": ans = doctor_report()
            elif x == "version": ans = f"BADSHAH-AI v{badshah_ai.__version__}"
            elif x == "migration guide": ans = migration_guide()
            elif x == "migration checklist": ans = migration_checklist()
            elif x == "repo validate": ans = repo_validate()
            elif x == "agents": ans = json.dumps(list_agents(), indent=2)
            elif x == "plugins": ans = json.dumps(list_plugins(), indent=2)
            elif x == "health check": ans = self.llm.health()
            else: ans = self.llm.generate(q)
            self.memory.remember(f"User: {q}\nAssistant: {ans}")
            self.tasks.add_task(q, "success", ans[:1000])
            return ans
        except Exception as e:
            self.tasks.add_task(q, "error", str(e))
            return "Error: " + str(e)
