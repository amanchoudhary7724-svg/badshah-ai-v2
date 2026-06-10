from badshah_ai.agents.base import BaseAgent
from badshah_ai.tools.browser_tools import open_url, search_web

class BrowserAgent(BaseAgent):
    name = "browser"

    def handle(self, query: str) -> str:
        q = query.lower().strip()
        if q.startswith("open "):
            return open_url(query.split(" ", 1)[1].strip())
        cleaned = query.replace("search web", "", 1).replace("search", "", 1).strip()
        return search_web(cleaned or query)
