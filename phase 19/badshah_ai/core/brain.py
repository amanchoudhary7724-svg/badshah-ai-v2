import json, re, badshah_ai
from badshah_ai.config.settings import settings
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.core.storage import SQLiteStore
from badshah_ai.core.memory_engine import MemoryEngine
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.tools.workspace_tools import create_website, write_file, read_file
from badshah_ai.tools.release_tools import export_workspace, release_package
from badshah_ai.tools.file_analysis_tools import pdf_text, excel_summary, ocr_image
from badshah_ai.tools.browser_tools import open_url, search_web
from badshah_ai.tools.browser_automation import browser_title, browser_text, browser_screenshot
from badshah_ai.tools.app_tools import open_app
from badshah_ai.tools.safety_tools import safety_policy, system_check, diagnostics_report, backup_config, restore_config

HELP = '''Commands:
help
version
safety
system check
diagnostics report
backup config
restore config
health check
remember ...
memory
memory search ...
forget memory
tasks
plugins
create website portfolio
write file notes.txt hello
read file notes.txt
pdf C:\\path\\file.pdf
excel C:\\path\\data.xlsx
ocr C:\\path\\image.png
search latest AI news
open https://github.com
browser title https://example.com
browser text https://example.com
browser screenshot https://example.com
open app notepad
export workspace
release package
'''

class Brain:
    def __init__(self):
        self.llm = OllamaClient(); self.tasks = SQLiteStore(); self.memory = MemoryEngine()
    def _extract_path(self, q, exts):
        for ext in exts:
            m = re.search(r'(.+\.' + ext + r')', q, re.I)
            if m: return m.group(1).strip().strip('"')
        return ""
    def _extract_url(self, q):
        m = re.search(r'(https?://\S+|www\.\S+|[\w.-]+\.[a-z]{2,}\S*)', q, re.I)
        return m.group(1) if m else ""
    def run(self, q: str) -> str:
        x = q.lower().strip()
        try:
            if x == "help": ans = HELP
            elif x == "version": ans = f"BADSHAH-AI v{badshah_ai.__version__}"
            elif x == "safety": ans = safety_policy()
            elif x == "system check": ans = system_check()
            elif x == "diagnostics report": ans = diagnostics_report()
            elif x == "backup config": ans = backup_config()
            elif x == "restore config": ans = restore_config()
            elif "health" in x: ans = self.llm.health()
            elif "validate env" in x: ans = "ENV OK" if settings.ollama_url.startswith("http") else "ENV issue"
            elif x == "plugins": ans = json.dumps(list_plugins(), indent=2)
            elif x.startswith("remember "): ans = self.memory.remember(q.split(" ", 1)[1], source="user")
            elif x == "memory":
                rows = self.memory.recent()
                ans = "\n".join([f"{t} | {src} | {txt}" for txt,src,t in rows]) or "No memory yet."
            elif x.startswith("memory search "):
                docs = self.memory.search(q.split(" ", 2)[2]); ans = "\n".join(docs) if docs else "No memory found."
            elif x == "forget memory": ans = self.memory.clear()
            elif x == "tasks":
                rows = self.tasks.recent_tasks(); ans = "\n".join([f"{t} | {s} | {qq}" for qq,s,r,t in rows]) or "No tasks yet."
            elif x.startswith("browser title"): ans = browser_title(self._extract_url(q))
            elif x.startswith("browser text"): ans = browser_text(self._extract_url(q))
            elif x.startswith("browser screenshot"): ans = browser_screenshot(self._extract_url(q))
            elif "create website" in x: ans = create_website(q.replace("create website","").strip())
            elif x.startswith("write file "):
                _, _, fn, content = q.split(" ", 3); ans = write_file(fn, content)
            elif x.startswith("read file "): ans = read_file(q.split(" ", 2)[2])
            elif x.startswith("pdf ") or ".pdf" in x: ans = pdf_text(self._extract_path(q, ["pdf"]))
            elif x.startswith("excel ") or ".xlsx" in x or ".xls" in x or ".csv" in x: ans = excel_summary(self._extract_path(q, ["xlsx","xls","csv"]))
            elif x.startswith("ocr ") or any(e in x for e in [".png",".jpg",".jpeg",".webp",".bmp"]): ans = ocr_image(self._extract_path(q, ["png","jpg","jpeg","webp","bmp"]), settings.tesseract_cmd)
            elif x.startswith("search "): ans = search_web(q[7:].strip())
            elif x.startswith("open app "): ans = open_app(q.replace("open app","").strip())
            elif x.startswith("open "): ans = open_url(q.split(" ",1)[1])
            elif "export workspace" in x: ans = export_workspace()
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
