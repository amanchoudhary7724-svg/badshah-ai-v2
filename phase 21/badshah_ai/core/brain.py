import json, badshah_ai
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.core.storage import SQLiteStore
from badshah_ai.core.memory_engine import MemoryEngine
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.agents.agent_registry import list_agents
from badshah_ai.tools.workspace_tools import create_website, write_file, read_file
from badshah_ai.tools.release_tools import release_package
from badshah_ai.tools.coding_tools import code_scan, explain_code, code_patch, run_tests, open_vscode

HELP = '''Commands:
help
version
agents
plugins
remember ...
memory
code scan
code explain main.py
code patch add dark mode to dashboard
code test
open vscode
create website portfolio
write file notes.txt hello
read file notes.txt
release package
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
            elif x.startswith("remember "): ans = self.memory.remember(q.split(" ",1)[1])
            elif x == "memory":
                rows = self.memory.recent()
                ans = "\n".join([f"{t} | {src} | {txt}" for txt,src,t in rows]) or "No memory yet."
            elif x == "code scan": ans = code_scan()
            elif x.startswith("code explain "): ans = explain_code(q.split(" ",2)[2])
            elif x.startswith("code patch "): ans = code_patch(q.split(" ",2)[2])
            elif x == "code test": ans = run_tests()
            elif x == "open vscode": ans = open_vscode()
            elif "create website" in x: ans = create_website(q.replace("create website","").strip())
            elif x.startswith("write file "):
                _, _, fn, content = q.split(" ",3); ans = write_file(fn, content)
            elif x.startswith("read file "): ans = read_file(q.split(" ",2)[2])
            elif "release package" in x: ans = release_package()
            else:
                context = "\n".join(self.memory.search(q, limit=3))
                ans = self.llm.generate(f"Relevant memory:\n{context}\n\nUser: {q}\nAssistant:")
            self.memory.remember(f"User: {q}\nAssistant: {ans}", source="chat")
            self.tasks.add_task(q, "success", ans[:1000])
            return ans
        except Exception as e:
            self.tasks.add_task(q, "error", str(e))
            return "Error: " + str(e)
