from badshah_ai.agents.base import BaseAgent

class BrowserAgent(BaseAgent):
    name = "browser"

    def handle(self, query: str) -> str:
        return (
            "Browser Agent ready hai. Phase 1 me safe placeholder enabled hai. "
            "Next phase me Playwright-based browser automation add hoga."
        )
