import json, badshah_ai
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.core.storage import SQLiteStore
from badshah_ai.core.memory_engine import MemoryEngine
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.agents.agent_registry import list_agents
from badshah_ai.tools.updater_tools import update_status, update_backup, update_pull, release_notes, github_push_guide

HELP = '''Commands:
help
version
agents
plugins
update status
update backup
update pull
release notes
github push guide
'''

class Brain:
    def __init__(self):
        self.llm = OllamaClient()
        self.tasks = SQLiteStore()
        self.memory = MemoryEngine()

    def run(self, q: str) -> str:
        x = q.lower().strip()
        try:
            if x == "help": ans = HELP
            elif x == "version": ans = f"BADSHAH-AI v{badshah_ai.__version__}"
            elif x == "plugins": ans = json.dumps(list_plugins(), indent=2)
            elif x == "agents": ans = json.dumps(list_agents(), indent=2)
            elif x == "update status": ans = update_status()
            elif x == "update backup": ans = update_backup()
            elif x == "update pull": ans = update_pull()
            elif x == "release notes": ans = release_notes()
            elif x == "github push guide": ans = github_push_guide()
            else: ans = self.llm.generate(q)
            self.memory.remember(f"User: {q}\nAssistant: {ans}")
            self.tasks.add_task(q, "success", ans[:1000])
            return ans
        except Exception as e:
            self.tasks.add_task(q, "error", str(e))
            return "Error: " + str(e)
