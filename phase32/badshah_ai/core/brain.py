import json, badshah_ai
from badshah_ai.models.llm_router import LLMRouter
from badshah_ai.core.storage import SQLiteStore
from badshah_ai.core.memory_engine import MemoryEngine
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.plugins.loader import PluginLoader
from badshah_ai.agents.agent_registry import list_agents
from badshah_ai.agents.planner import MultiAgentPlanner
from badshah_ai.tools.doctor import doctor_report
from badshah_ai.tools.workspace_tools import create_website, write_file, read_file
from badshah_ai.tools.communication_tools import create_draft, show_drafts
from badshah_ai.tools.screen_vision_tools import screen_safety, take_screenshot
from badshah_ai.tools.qa_tools import smoke_test, perf_check, qa_checklist, error_report
from badshah_ai.tools.release_tools import release_package

HELP = '''BADSHAH-AI v3.2 Commands:
doctor | help | version | agents | plugins
models | model health | ask coding ...
remember ... | memory | memory search ...
plan ... | run plan ...
plugin marketplace | plugin enable custom_notes | custom note ...
draft whatsapp Aman hello | show drafts
screen safety | screen shot
test smoke | perf check | qa checklist | error report
create website portfolio | write file notes.txt hello | read file notes.txt
release package
'''

class Brain:
    def __init__(self):
        self.router = LLMRouter()
        self.tasks = SQLiteStore()
        self.memory = MemoryEngine()
        self.plugins = PluginLoader()
        self.planner = MultiAgentPlanner()

    def execute_single(self, q):
        x = q.lower().strip()
        routed = self.plugins.route(q)
        if routed is not None: return routed
        if x == "doctor": return doctor_report()
        if x == "help": return HELP
        if x == "version": return f"BADSHAH-AI v{badshah_ai.__version__}"
        if x == "agents": return json.dumps(list_agents(), indent=2)
        if x == "plugins": return json.dumps(list_plugins(), indent=2)
        if x == "models": return self.router.list_models_config()
        if x == "model health": return self.router.health()
        if x.startswith("ask "):
            parts = q.split(" ", 2)
            return self.router.generate(parts[2], parts[1]) if len(parts) >= 3 else "Usage: ask coding question"
        if x.startswith("remember "): return self.memory.remember(q.split(" ", 1)[1], "user")
        if x == "memory":
            rows = self.memory.recent()
            return "\n".join([f"{t} | {src} | {txt}" for txt, src, t in rows]) or "No memory."
        if x.startswith("memory search "):
            return "\n".join(self.memory.search(q.split(" ", 2)[2])) or "No memory found."
        if x == "plugin marketplace": return self.plugins.marketplace_text()
        if x.startswith("plugin enable "): return self.plugins.enable(q.split(" ", 2)[2])
        if x.startswith("draft "):
            parts = q.split(" ", 3)
            return create_draft(parts[1], parts[2], parts[3]) if len(parts) >= 4 else "Usage: draft whatsapp TARGET message"
        if x == "show drafts": return show_drafts()
        if x == "screen safety": return screen_safety()
        if x == "screen shot": return take_screenshot()
        if x == "test smoke": return smoke_test()
        if x == "perf check": return perf_check()
        if x == "qa checklist": return qa_checklist()
        if x == "error report": return error_report()
        if "create website" in x: return create_website(q.replace("create website", "").strip())
        if x.startswith("write file "):
            _, _, fn, content = q.split(" ", 3)
            return write_file(fn, content)
        if x.startswith("read file "): return read_file(q.split(" ", 2)[2])
        if x == "release package": return release_package()
        return self.router.generate(q)

    def run(self, q):
        x = q.lower().strip()
        try:
            if x.startswith("plan "):
                steps = self.planner.make_plan(q.split(" ", 1)[1])
                ans = self.planner.format_plan(steps)
            elif x.startswith("run plan "):
                steps = self.planner.make_plan(q.split(" ", 2)[2])
                outputs = [self.planner.format_plan(steps), ""]
                for i, s in enumerate(steps, 1):
                    outputs.append(f"Step {i} [{s['agent']}]: {self.execute_single(s['task'])}")
                ans = "\n".join(outputs)
            else:
                ans = self.execute_single(q)
            self.memory.remember(f"User: {q}\nAssistant: {ans}", "chat")
            self.tasks.add_task(q, "success", ans[:1000])
            return ans
        except Exception as e:
            self.tasks.add_task(q, "error", str(e))
            return "Error: " + str(e)
