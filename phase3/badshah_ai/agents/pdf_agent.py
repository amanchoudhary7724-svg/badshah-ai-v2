import re
from badshah_ai.agents.base import BaseAgent
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.tools.pdf_tools import extract_pdf_text

class PDFAgent(BaseAgent):
    name = "pdf"

    def __init__(self) -> None:
        self.llm = OllamaClient()

    def handle(self, query: str) -> str:
        path = self._extract_path(query)
        if not path:
            return "PDF path do. Example: read pdf C:\\Users\\SOURBH\\Desktop\\file.pdf"
        text = extract_pdf_text(path)
        if "summar" in query.lower() or "summary" in query.lower():
            return self.llm.generate("Summarize this PDF text clearly:\n\n" + text)
        return text

    def _extract_path(self, query: str) -> str:
        match = re.search(r'(?i)(?:pdf|file)\s+(.+?\.pdf)', query)
        if match:
            return match.group(1).strip().strip('"')
        if query.lower().strip().endswith(".pdf"):
            return query.strip().strip('"')
        return ""
