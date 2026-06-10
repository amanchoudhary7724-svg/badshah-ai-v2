import json, badshah_ai
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.core.storage import SQLiteStore
from badshah_ai.core.memory_engine import MemoryEngine
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.agents.agent_registry import list_agents
from badshah_ai.tools.screen_vision_tools import take_screenshot, screen_ocr, image_ocr, screen_safety, desktop_action

HELP = '''Commands:
help
version
agents
plugins
screen shot
screen ocr
image ocr C:\\path\\image.png
screen safety
desktop action open notepad
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
            elif x == "screen shot": ans = take_screenshot()
            elif x == "screen ocr": ans = screen_ocr()
            elif x.startswith("image ocr "): ans = image_ocr(q.split(" ", 2)[2])
            elif x == "screen safety": ans = screen_safety()
            elif x.startswith("desktop action "): ans = desktop_action(q.replace("desktop action", "", 1).strip())
            else: ans = self.llm.generate(q)
            self.memory.remember(f"User: {q}\nAssistant: {ans}", source="chat")
            self.tasks.add_task(q, "success", ans[:1000])
            return ans
        except Exception as e:
            self.tasks.add_task(q, "error", str(e))
            return "Error: " + str(e)
