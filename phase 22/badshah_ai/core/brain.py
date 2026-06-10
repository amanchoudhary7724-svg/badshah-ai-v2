import json, badshah_ai
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.core.storage import SQLiteStore
from badshah_ai.core.memory_engine import MemoryEngine
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.agents.agent_registry import list_agents
from badshah_ai.tools.communication_tools import add_contact, list_contacts, create_draft, show_drafts
from badshah_ai.tools.workspace_tools import write_file, read_file

HELP = '''Commands:
help
version
agents
plugins
contacts
add contact Aman +919999999999
draft whatsapp Aman hello
draft email client project update
draft telegram team deployment done
draft discord devs bug fixed
show drafts
write file notes.txt hello
read file notes.txt
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
                if len(parts) < 4:
                    ans = "Usage: add contact NAME PHONE_OR_EMAIL"
                else:
                    _, _, name, value = parts
                    ans = add_contact(name, value)
            elif x.startswith("draft "):
                parts = q.split(" ", 3)
                if len(parts) < 4:
                    ans = "Usage: draft whatsapp TARGET message"
                else:
                    _, channel, target, message = parts
                    if channel.lower() not in {"whatsapp","email","telegram","discord"}:
                        ans = "Supported: whatsapp, email, telegram, discord"
                    else:
                        ans = create_draft(channel, target, message)
            elif x == "show drafts": ans = show_drafts()
            elif x.startswith("remember "): ans = self.memory.remember(q.split(" ",1)[1])
            elif x.startswith("write file "):
                _, _, fn, content = q.split(" ",3); ans = write_file(fn, content)
            elif x.startswith("read file "): ans = read_file(q.split(" ",2)[2])
            else:
                ans = self.llm.generate(q)
            self.memory.remember(f"User: {q}\nAssistant: {ans}", source="chat")
            self.tasks.add_task(q, "success", ans[:1000])
            return ans
        except Exception as e:
            self.tasks.add_task(q, "error", str(e))
            return "Error: " + str(e)
