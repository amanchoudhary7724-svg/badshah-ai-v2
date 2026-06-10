import badshah_ai
from badshah_ai.config.settings import settings
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.tools.project_tools import create_website
from badshah_ai.tools.release_tools import release_package

HELP = '''Commands:
help
version
health check
validate env
create website portfolio
release package
'''

class Brain:
    def __init__(self):
        self.llm = OllamaClient()

    def run(self, q: str) -> str:
        x = q.lower().strip()
        if x == "help":
            return HELP
        if x == "version":
            return f"BADSHAH-AI v{badshah_ai.__version__}"
        if "health" in x:
            return self.llm.health()
        if "validate env" in x:
            return "ENV OK" if settings.ollama_url.startswith("http") else "ENV issue"
        if "create website" in x:
            return create_website(q.replace("create website", "").strip())
        if "release package" in x:
            return release_package()
        return self.llm.generate(q)
