from badshah_ai.agents.base import BaseAgent

class VisionAgent(BaseAgent):
    name = "vision"

    def handle(self, query: str) -> str:
        return (
            "Vision Agent ready hai. Phase 1 me placeholder enabled hai. "
            "Next phase me OCR/screenshot/image analysis add hoga."
        )
