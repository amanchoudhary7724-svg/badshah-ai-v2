import json
import badshah_ai
from badshah_ai.core.help_text import HELP_TEXT
from badshah_ai.core.memory import Memory
from badshah_ai.core.task_history import TaskHistory
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.tools.health_tools import validate_env, health_check, smoke_test
from badshah_ai.tools.project_tools import create_static_website
from badshah_ai.tools.export_tools import release_package

class Brain:
    def __init__(self):
        self.memory = Memory()
        self.tasks = TaskHistory()
        self.llm = OllamaClient()

    def run(self, q):
        x = q.lower().strip()
        if x == "help":
            ans, tag = HELP_TEXT, "help"
        elif x == "version":
            ans, tag = f"BADSHAH-AI v{badshah_ai.__version__}", "version"
        elif x == "plugins":
            ans, tag = json.dumps(list_plugins(), indent=2), "plugins"
        elif "validate env" in x:
            ans, tag = validate_env(), "env"
        elif "health" in x:
            ans, tag = health_check(), "health"
        elif "smoke test" in x:
            ans, tag = smoke_test(), "smoke"
        elif "create website" in x:
            ans, tag = create_static_website(q.replace("create website","").strip()), "project"
        elif "release package" in x:
            ans, tag = release_package(), "release"
        elif x == "status":
            ans, tag = f"Version: {badshah_ai.__version__}\n{health_check()}", "status"
        else:
            ans, tag = self.llm.generate(q), "chat"

        self.memory.store(q, ans, tag)
        self.tasks.add(q, tag, "success", ans[:1000])
        return ans
