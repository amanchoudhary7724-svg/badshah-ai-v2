import re
from badshah_ai.agents.base import BaseAgent
from badshah_ai.tools.excel_tools import summarize_table

class ExcelAgent(BaseAgent):
    name = "excel"

    def handle(self, query: str) -> str:
        path = self._extract_path(query)
        if not path:
            return "Excel/CSV path do. Example: analyze excel C:\\Users\\SOURBH\\Desktop\\data.xlsx"
        return summarize_table(path)

    def _extract_path(self, query: str) -> str:
        match = re.search(r'(?i)(?:excel|csv|file|analyze)\s+(.+?\.(?:xlsx|xls|csv))', query)
        if match:
            return match.group(1).strip().strip('"')
        if query.lower().strip().endswith((".xlsx", ".xls", ".csv")):
            return query.strip().strip('"')
        return ""
