from badshah_ai.agents.coding_agent import CodingAgent
from badshah_ai.agents.excel_agent import ExcelAgent
from badshah_ai.agents.pdf_agent import PDFAgent
from badshah_ai.agents.browser_agent import BrowserAgent
from badshah_ai.agents.vision_agent import VisionAgent

class Router:
    def __init__(self) -> None:
        self.coding = CodingAgent()
        self.excel = ExcelAgent()
        self.pdf = PDFAgent()
        self.browser = BrowserAgent()
        self.vision = VisionAgent()

    def route(self, query: str):
        q = query.lower()
        if any(k in q for k in ["code", "python", "website", "app", "script", "program", "build"]):
            return self.coding
        if any(k in q for k in ["excel", "csv", "spreadsheet", "data analysis"]):
            return self.excel
        if "pdf" in q:
            return self.pdf
        if any(k in q for k in ["browser", "search", "website open", "web"]):
            return self.browser
        if any(k in q for k in ["image", "ocr", "screenshot", "vision"]):
            return self.vision
        return None
