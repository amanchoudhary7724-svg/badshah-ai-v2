from badshah_ai.agents.coding_agent import CodingAgent
from badshah_ai.agents.excel_agent import ExcelAgent
from badshah_ai.agents.pdf_agent import PDFAgent
from badshah_ai.agents.browser_agent import BrowserAgent
from badshah_ai.agents.vision_agent import VisionAgent
from badshah_ai.agents.app_agent import AppAgent
from badshah_ai.agents.email_agent import EmailAgent
from badshah_ai.agents.whatsapp_agent import WhatsAppAgent
from badshah_ai.core.planner import Planner

class Router:
    def __init__(self) -> None:
        self.planner = Planner()
        self.agents = {
            "coding": CodingAgent(),
            "project_generator": CodingAgent(),
            "excel": ExcelAgent(),
            "pdf": PDFAgent(),
            "browser": BrowserAgent(),
            "vision": VisionAgent(),
            "apps": AppAgent(),
            "email": EmailAgent(),
            "whatsapp": WhatsAppAgent(),
        }

    def route(self, query: str):
        kind = self.planner.classify(query)
        return self.agents.get(kind)
