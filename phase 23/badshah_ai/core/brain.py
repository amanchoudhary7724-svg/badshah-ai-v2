import json, badshah_ai
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.core.storage import SQLiteStore
from badshah_ai.core.memory_engine import MemoryEngine
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.agents.agent_registry import list_agents
from badshah_ai.tools.google_productivity_tools import (
    add_contact, list_contacts, email_draft, followup_email, meeting_invite,
    calendar_draft, show_drafts, show_calendar_drafts
)

HELP = '''Commands:
help
version
agents
plugins
add contact Aman aman@example.com
contacts
draft email Aman project update
followup email Aman quotation pending
meeting invite Aman product demo Friday 4pm
calendar draft Team Meeting tomorrow 5pm
show drafts
show calendar drafts
'''

class Brain:
    def __init__(self):
        self.llm = OllamaClient()
        self.tasks = SQLiteStore()
        self.memory = MemoryEngine()

    def run(self, q: str) -> str:
        x = q.lower().strip()
        try:
            if x == "help": ans = HELP
            elif x == "version": ans = f"BADSHAH-AI v{badshah_ai.__version__}"
            elif x == "plugins": ans = json.dumps(list_plugins(), indent=2)
            elif x == "agents": ans = json.dumps(list_agents(), indent=2)
            elif x == "contacts": ans = list_contacts()
            elif x.startswith("add contact "):
                parts = q.split(" ", 3)
                ans = add_contact(parts[2], parts[3]) if len(parts) >= 4 else "Usage: add contact NAME EMAIL_OR_PHONE"
            elif x.startswith("draft email "):
                parts = q.split(" ", 3)
                ans = email_draft(parts[2], parts[3]) if len(parts) >= 4 else "Usage: draft email TARGET message"
            elif x.startswith("followup email "):
                parts = q.split(" ", 3)
                ans = followup_email(parts[2], parts[3]) if len(parts) >= 4 else "Usage: followup email TARGET topic"
            elif x.startswith("meeting invite "):
                parts = q.split(" ", 3)
                ans = meeting_invite(parts[2], parts[3]) if len(parts) >= 4 else "Usage: meeting invite TARGET topic/time"
            elif x.startswith("calendar draft "):
                payload = q.split(" ", 2)[2] if len(q.split(" ", 2)) >= 3 else ""
                ans = calendar_draft(payload[:80] or "Untitled Event", payload)
            elif x == "show drafts": ans = show_drafts()
            elif x == "show calendar drafts": ans = show_calendar_drafts()
            else:
                ans = self.llm.generate(q)
            self.memory.remember(f"User: {q}\nAssistant: {ans}", source="chat")
            self.tasks.add_task(q, "success", ans[:1000])
            return ans
        except Exception as e:
            self.tasks.add_task(q, "error", str(e))
            return "Error: " + str(e)
