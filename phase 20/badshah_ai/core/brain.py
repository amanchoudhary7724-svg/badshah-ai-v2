import json, re, badshah_ai
from badshah_ai.config.settings import settings
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.core.storage import SQLiteStore
from badshah_ai.core.memory_engine import MemoryEngine
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.agents.agent_registry import list_agents
from badshah_ai.agents.planner import MultiAgentPlanner
from badshah_ai.tools.workspace_tools import create_website, write_file, read_file
from badshah_ai.tools.release_tools import export_workspace, release_package
from badshah_ai.tools.file_analysis_tools import pdf_text, excel_summary
from badshah_ai.tools.browser_tools import open_url, search_web
from badshah_ai.tools.safety_tools import safety_policy, system_check

HELP = '''Commands:
help
version
agents
planner status
plan create website portfolio and remember project name
run plan create website portfolio and export workspace
remember ...
memory
memory search ...
tasks
plugins
create website portfolio
write file notes.txt hello
read file notes.txt
pdf C:\\path\\file.pdf
excel C:\\path\\data.xlsx
search latest AI news
open https://github.com
export workspace
release package
'''

class Brain:
    def __init__(self):
        self.llm = OllamaClient()
        self.tasks = SQLiteStore()
        self.memory = MemoryEngine()
        self.planner = MultiAgentPlanner()

    def _extract_path(self, q, exts):
        for ext in exts:
            m = re.search(r'(.+\.' + ext + r')', q, re.I)
            if m: return m.group(1).strip().strip('"')
        return ""

    def execute_single(self, q: str):
        x = q.lower().strip()
        if x == "help": return HELP
        if x == "version": return f"BADSHAH-AI v{badshah_ai.__version__}"
        if x == "agents": return self.planner.list_agents_text()
        if x == "planner status": return "Planner OK\n" + self.planner.list_agents_text()
        if "health" in x: return self.llm.health()
        if x == "safety": return safety_policy()
        if x == "system check": return system_check()
        if x == "plugins": return json.dumps(list_plugins(), indent=2)
        if x.startswith("remember "): return self.memory.remember(q.split(" ", 1)[1], source="user")
        if x == "memory":
            rows = self.memory.recent()
            return "\n".join([f"{t} | {src} | {txt}" for txt,src,t in rows]) or "No memory yet."
        if x.startswith("memory search "):
            docs = self.memory.search(q.split(" ", 2)[2])
            return "\n".join(docs) if docs else "No memory found."
        if x == "forget memory": return self.memory.clear()
        if x == "tasks":
            rows = self.tasks.recent_tasks()
            return "\n".join([f"{t} | {s} | {qq}" for qq,s,r,t in rows]) or "No tasks yet."
        if "create website" in x: return create_website(q.replace("create website","").strip())
        if x.startswith("write file "):
            _, _, fn, content = q.split(" ", 3); return write_file(fn, content)
        if x.startswith("read file "): return read_file(q.split(" ", 2)[2])
        if x.startswith("pdf ") or ".pdf" in x: return pdf_text(self._extract_path(q, ["pdf"]))
        if x.startswith("excel ") or ".xlsx" in x or ".xls" in x or ".csv" in x: return excel_summary(self._extract_path(q, ["xlsx","xls","csv"]))
        if x.startswith("search "): return search_web(q[7:].strip())
        if x.startswith("open "): return open_url(q.split(" ",1)[1])
        if "export workspace" in x: return export_workspace()
        if "release package" in x: return release_package()
        context = "\n".join(self.memory.search(q, limit=3))
        return self.llm.generate(f"Relevant memory:\n{context}\n\nUser: {q}\nAssistant:")

    def run(self, q: str) -> str:
        x = q.lower().strip()
        try:
            if x.startswith("plan "):
                steps = self.planner.make_plan(q.split(" ", 1)[1])
                ans = self.planner.format_plan(steps)
            elif x.startswith("run plan "):
                request = q.split(" ", 2)[2]
                steps = self.planner.make_plan(request)
                outputs = [self.planner.format_plan(steps), ""]
                for i, step in enumerate(steps, 1):
                    result = self.execute_single(step["task"])
                    outputs.append(f"Step {i} [{step['agent']}]: {result}")
                ans = "\n".join(outputs)
            else:
                ans = self.execute_single(q)
            self.memory.remember(f"User: {q}\nAssistant: {ans}", source="chat")
            self.tasks.add_task(q, "success", ans[:1000])
            return ans
        except Exception as e:
            self.tasks.add_task(q, "error", str(e))
            return "Error: " + str(e)
