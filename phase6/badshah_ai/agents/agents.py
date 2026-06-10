import re
from badshah_ai.agents.base import BaseAgent
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.tools.file_tools import write_text_file, read_text_file
from badshah_ai.tools.project_tools import create_static_website
from badshah_ai.tools.export_tools import export_workspace, backup_workspace
from badshah_ai.tools.browser_tools import open_url, search_web, scrape
from badshah_ai.tools.pdf_tools import extract_pdf_text
from badshah_ai.tools.excel_tools import summarize_table
from badshah_ai.tools.ocr_tools import extract_image_text
from badshah_ai.tools.app_tools import open_app
from badshah_ai.tools.health_tools import health_check
from badshah_ai.tools.selfmod_tools import propose_self_modification, list_patches, apply_latest_patch
from badshah_ai.core.task_history import TaskHistory

class HealthAgent(BaseAgent):
    name = "health"
    def handle(self,q): return health_check()

class SelfModAgent(BaseAgent):
    name = "selfmod"
    def handle(self,q): return propose_self_modification(q)

class ApplyPatchAgent(BaseAgent):
    name = "apply_patch"
    def handle(self,q): return apply_latest_patch()

class PatchListAgent(BaseAgent):
    name = "patches"
    def handle(self,q): return list_patches()

class BackupAgent(BaseAgent):
    name = "backup"
    def handle(self,q): return backup_workspace()

class ChatAgent(BaseAgent):
    name = "chat"
    def __init__(self): self.llm = OllamaClient()
    def handle(self,q): return self.llm.generate(q)

class CodingAgent(BaseAgent):
    name = "coding"
    def __init__(self): self.llm = OllamaClient()
    def handle(self,q):
        x = q.lower()
        if x.startswith("write file "):
            _,_,fn,content = q.split(" ",3)
            return write_text_file(fn,content)
        if x.startswith("read file "):
            return read_text_file(q.split(" ",2)[2])
        if "create website" in x or "make website" in x:
            return create_static_website(q.replace("create website","").replace("make website","").strip())
        return self.llm.generate("Write code for: " + q)

class ExportAgent(BaseAgent):
    name = "export"
    def handle(self,q): return export_workspace()

class TaskAgent(BaseAgent):
    name = "tasks"
    def handle(self,q):
        rows = TaskHistory().recent(10)
        return "\n".join([f"{r['created_at']} | {r['agent']} | {r['query']}" for r in rows]) or "No tasks."

class BrowserAgent(BaseAgent):
    name = "browser"
    def handle(self,q):
        x = q.lower()
        if "scrape" in x:
            m = re.search(r'(https?://\S+|www\.\S+|[\w.-]+\.[a-z]{2,}\S*)',q)
            return scrape(m.group(1)) if m else "URL missing"
        if x.startswith("open "):
            return open_url(q.split(" ",1)[1])
        return search_web(q.replace("search","").strip())

class PDFAgent(BaseAgent):
    name = "pdf"
    def handle(self,q):
        m = re.search(r'(.+\.pdf)',q,re.I)
        return extract_pdf_text(m.group(1).strip().strip('"')) if m else "PDF path missing"

class ExcelAgent(BaseAgent):
    name = "excel"
    def handle(self,q):
        m = re.search(r'(.+\.(xlsx|xls|csv))',q,re.I)
        return summarize_table(m.group(1).strip().strip('"')) if m else "Excel/CSV path missing"

class VisionAgent(BaseAgent):
    name = "vision"
    def handle(self,q):
        m = re.search(r'(.+\.(png|jpg|jpeg|webp|bmp))',q,re.I)
        return extract_image_text(m.group(1).strip().strip('"')) if m else "Image path missing"

class AppAgent(BaseAgent):
    name = "apps"
    def handle(self,q): return open_app(q.lower().replace("open app","").strip())

class DraftAgent(BaseAgent):
    name = "draft"
    def handle(self,q):
        fn = "drafts/whatsapp_draft.txt" if "whatsapp" in q.lower() else "drafts/email_draft.txt"
        return write_text_file(fn,q)
