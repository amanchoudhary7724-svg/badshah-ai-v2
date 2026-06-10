import json, badshah_ai
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.core.storage import SQLiteStore
from badshah_ai.core.memory_engine import MemoryEngine
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.agents.agent_registry import list_agents
from badshah_ai.tools.qa_tools import smoke_test, perf_check, error_report, qa_checklist
from badshah_ai.tools.workspace_tools import create_website
from badshah_ai.tools.release_tools import release_package

HELP = '''Commands:
help
version
agents
plugins
health check
test smoke
perf check
error report
qa checklist
create website portfolio
release package
build exe guide
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
            elif x == "health check": ans = self.llm.health()
            elif x == "test smoke": ans = smoke_test()
            elif x == "perf check": ans = perf_check()
            elif x == "error report": ans = error_report()
            elif x == "qa checklist": ans = qa_checklist()
            elif "create website" in x: ans = create_website(q.replace("create website", "").strip())
            elif x == "release package": ans = release_package()
            elif x == "build exe guide": ans = "Run: installer\\BUILD_EXE.bat\nOutput: dist\\BADSHAH-AI\\BADSHAH-AI.exe"
            else: ans = self.llm.generate(q)
            self.memory.remember(f"User: {q}\nAssistant: {ans}")
            self.tasks.add_task(q, "success", ans[:1000])
            return ans
        except Exception as e:
            self.tasks.add_task(q, "error", str(e))
            return "Error: " + str(e)
