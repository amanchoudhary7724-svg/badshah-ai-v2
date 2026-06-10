import re
from badshah_ai.agents.base import BaseAgent
from badshah_ai.tools.ocr_tools import extract_image_text

class VisionAgent(BaseAgent):
    name = "vision"

    def handle(self, query: str) -> str:
        path = self._extract_path(query)
        if not path:
            return "Image path do. Example: ocr image C:\\Users\\SOURBH\\Desktop\\image.png"
        return extract_image_text(path)

    def _extract_path(self, query: str) -> str:
        match = re.search(r'(?i)(?:image|ocr|screenshot|file)\s+(.+?\.(?:png|jpg|jpeg|webp|bmp))', query)
        if match:
            return match.group(1).strip().strip('"')
        if query.lower().strip().endswith((".png", ".jpg", ".jpeg", ".webp", ".bmp")):
            return query.strip().strip('"')
        return ""
