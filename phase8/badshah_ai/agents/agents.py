import re
import json
from badshah_ai.agents.base import BaseAgent
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.config.settings import settings
from badshah_ai.core.help_text import HELP_TEXT
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.tools.file_tools import write_text_file, read_text_file
from badshah_ai.tools.project_tools import create_static_website
from badshah_ai.tools.export_tools import export_workspace, backup_workspace, release_package
from badshah_ai.tools.status_tools import version, changelog, status_report
from badshah_ai.tools.browser_tools import open_url, search_web, scrape
from badshah_ai.tools.pdf_tools import extract_pdf_text
from badshah_ai.tools.excel_tools import summarize_table
from badshah_ai.tools.ocr_tools import extract_image_text
from badshah_ai.tools.app_tools import open_app
from badshah_ai.tools.health_tools import health_check, diagnostics
from badshah_ai.tools.selfmod_tools import propose_self_modification, list_patches, apply_latest_patch
from badshah_ai.core.task_history import TaskHistory

class SimpleAgent(BaseAgent):
    def __init__(self, name, fn):
        self.name = name
        self.fn = fn
    def handle(self, q):
        return self.fn(q)

def help_fn(q): return HELP_TEXT
def config_fn(q): return json.dumps(settings.as_dict(), indent=2)
def plugins_fn(q): return json.dumps(list_plugins(), indent=2)
def tasks_fn(q):
    rows = TaskHistory().recent(10)
    return "\n".join([f"{r['created_at']} | {r['agent']} | {r['query']}" for r in rows]) or "No tasks."

def coding_fn(q):
    x = q.lower()
    if x.startswith("write file "):
        _,_,fn,content = q.split(" ",3)
        return write_text_file(fn, content)
    if x.startswith("read file "):
        return read_text_file(q.split(" ",2)[2])
    if "create website" in x or "make website" in x:
        return create_static_website(q.replace("create website","").replace("make website","").strip())
    return OllamaClient().generate("Write code for: " + q)

def browser_fn(q):
    x = q.lower()
    if "scrape" in x:
        m = re.search(r'(https?://\S+|www\.\S+|[\w.-]+\.[a-z]{2,}\S*)', q)
        return scrape(m.group(1)) if m else "URL missing"
    if x.startswith("open "):
        return open_url(q.split(" ",1)[1])
    return search_web(q.replace("search","").strip())

def pdf_fn(q):
    m = re.search(r'(.+\.pdf)', q, re.I)
    return extract_pdf_text(m.group(1).strip().strip('"')) if m else "PDF path missing"

def excel_fn(q):
    m = re.search(r'(.+\.(xlsx|xls|csv))', q, re.I)
    return summarize_table(m.group(1).strip().strip('"')) if m else "Excel/CSV path missing"

def vision_fn(q):
    m = re.search(r'(.+\.(png|jpg|jpeg|webp|bmp))', q, re.I)
    return extract_image_text(m.group(1).strip().strip('"')) if m else "Image path missing"

def app_fn(q): return open_app(q.lower().replace("open app","").strip())

def draft_fn(q):
    fn = "drafts/whatsapp_draft.txt" if "whatsapp" in q.lower() else "drafts/email_draft.txt"
    return write_text_file(fn, q)
