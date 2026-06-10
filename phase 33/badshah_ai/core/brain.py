import json
import badshah_ai
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.core.storage import SQLiteStore
from badshah_ai.core.memory_engine import MemoryEngine
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.agents.agent_registry import list_agents
from badshah_ai.tools.doctor import doctor_report
from badshah_ai.tools.repo_tools import repo_tree, github_guide, release_notes, smoke_test

HELP = '''BADSHAH-AI v3.3 Commands:
doctor
version
repo tree
github guide
release notes
test smoke
agents
plugins
health check
remember ...
memory
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
            elif x == "repo tree": ans = repo_tree()
            elif x == "github guide": ans = github_guide()
            elif x == "release notes": ans = release_notes()
            elif x == "test smoke": ans = smoke_test()
            elif x == "agents": ans = json.dumps(list_agents(), indent=2)
            elif x == "plugins": ans = json.dumps(list_plugins(), indent=2)
            elif x == "health check": ans = self.llm.health()
            elif x.startswith("remember "): ans = self.memory.remember(q.split(" ", 1)[1], "user")
            elif x == "memory":
                rows = self.memory.recent()
                ans = "\n".join([f"{t} | {src} | {txt}" for txt, src, t in rows]) or "No memory."
            else:
                ans = self.llm.generate(q)
            self.memory.remember(f"User: {q}\nAssistant: {ans}", "chat")
            self.tasks.add_task(q, "success", ans[:1000])
            return ans
        except Exception as e:
            self.tasks.add_task(q, "error", str(e))
            return "Error: " + str(e)
