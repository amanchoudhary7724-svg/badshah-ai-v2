from badshah_ai.agents.base import BaseAgent

class ExcelAgent(BaseAgent):
    name = "excel"

    def handle(self, query: str) -> str:
        return (
            "Excel Agent ready hai. Phase 1 me basic routing enabled hai. "
            "Next phase me CSV/XLSX read, analysis, charts aur report generation add hoga."
        )
