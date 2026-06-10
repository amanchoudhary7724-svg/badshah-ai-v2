import json, badshah_ai
from badshah_ai.models.llm_router import LLMRouter
from badshah_ai.core.storage import SQLiteStore
from badshah_ai.core.memory_engine import MemoryEngine
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.plugins.loader import PluginLoader
from badshah_ai.tools.workspace_tools import create_website

HELP = '''Commands:
help
version
plugins
plugin marketplace
plugin enable custom_notes
plugin disable custom_notes
custom note hello from plugin
models
ask coding write python function
create website portfolio
'''

class Brain:
    def __init__(self):
        self.router = LLMRouter()
        self.tasks = SQLiteStore()
        self.memory = MemoryEngine()
        self.plugins = PluginLoader()

    def run(self, q: str) -> str:
        x = q.lower().strip()
        try:
            routed = self.plugins.route(q)
            if routed is not None:
                ans = routed
            elif x == "help": ans = HELP
            elif x == "version": ans = f"BADSHAH-AI v{badshah_ai.__version__}"
            elif x == "plugins": ans = json.dumps(list_plugins(), indent=2)
            elif x == "plugin marketplace": ans = self.plugins.marketplace_text()
            elif x.startswith("plugin enable "): ans = self.plugins.enable(q.split(" ", 2)[2].strip())
            elif x.startswith("plugin disable "): ans = self.plugins.disable(q.split(" ", 2)[2].strip())
            elif x == "models": ans = self.router.list_models_config()
            elif x.startswith("ask "):
                parts = q.split(" ", 2)
                ans = self.router.generate(parts[2], role=parts[1]) if len(parts) >= 3 else "Usage: ask coding your question"
            elif "create website" in x:
                ans = create_website(q.replace("create website","").strip())
            else:
                ans = self.router.generate(q)
            self.memory.remember(f"User: {q}\nAssistant: {ans}")
            self.tasks.add_task(q, "success", ans[:1000])
            return ans
        except Exception as e:
            self.tasks.add_task(q, "error", str(e))
            return "Error: " + str(e)
