from badshah_ai.agents.base import BaseAgent

class PDFAgent(BaseAgent):
    name = "pdf"

    def handle(self, query: str) -> str:
        return (
            "PDF Agent ready hai. Phase 1 me basic routing enabled hai. "
            "Next phase me PDF text extraction, summary aur PDF generation add hoga."
        )
