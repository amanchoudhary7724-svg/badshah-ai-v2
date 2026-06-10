from badshah_ai.agents.base import BaseAgent
from badshah_ai.tools.file_tools import write_text_file

class WhatsAppAgent(BaseAgent):
    name = "whatsapp"

    def handle(self, query: str) -> str:
        # Safe Phase 3: creates draft only, no auto-send.
        return write_text_file("drafts/whatsapp_draft.txt", query)
