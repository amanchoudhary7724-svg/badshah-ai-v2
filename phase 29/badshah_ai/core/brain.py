import json, badshah_ai
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.core.storage import SQLiteStore
from badshah_ai.core.memory_engine import MemoryEngine
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.agents.agent_registry import list_agents
from badshah_ai.tools.qa_tools import smoke_test, run_all_tests, perf_check, dependency_audit, error_report, bug_template, qa_checklist

HELP = '''Commands:
help
version
agents
plugins
test smoke
test all
perf check
dependency audit
error report
bug template
qa checklist
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
            elif x == "test smoke": ans = smoke_test()
            elif x == "test all": ans = run_all_tests()
            elif x == "perf check": ans = perf_check()
            elif x == "dependency audit": ans = dependency_audit()
            elif x == "error report": ans = error_report()
            elif x == "bug template": ans = bug_template()
            elif x == "qa checklist": ans = qa_checklist()
            else: ans = self.llm.generate(q)
            self.memory.remember(f"User: {q}\nAssistant: {ans}")
            self.tasks.add_task(q, "success", ans[:1000])
            return ans
        except Exception as e:
            self.tasks.add_task(q, "error", str(e))
            return "Error: " + str(e)
