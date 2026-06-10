from badshah_ai.agents.base import BaseAgent

class VisionAgent(BaseAgent):
    name = "vision"

    def handle(self, query: str) -> str:
        return (
            "Vision Agent Phase 2 ready hai. OCR/Image analysis Phase 3 me add hoga. "
            "Abhi PDF/Excel/Browser/File tools active hain."
        )
