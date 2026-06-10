from badshah_ai.agents.base import BaseAgent
from badshah_ai.tools.app_tools import open_app

class AppAgent(BaseAgent):
    name = "apps"

    def handle(self, query: str) -> str:
        q = query.lower().replace("open app", "").replace("launch app", "").strip()
        if not q:
            return "App name do. Example: open app notepad"
        return open_app(q)
