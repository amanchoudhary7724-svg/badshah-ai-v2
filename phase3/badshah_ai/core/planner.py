class Planner:
    def classify(self, query: str) -> str:
        q = query.lower()
        if any(k in q for k in ["create website", "make website", "portfolio", "landing page"]):
            return "project_generator"
        if any(k in q for k in ["email", "mail"]):
            return "email"
        if "whatsapp" in q:
            return "whatsapp"
        if any(k in q for k in ["open app", "launch app"]):
            return "apps"
        if any(k in q for k in ["excel", "csv", "spreadsheet", ".xlsx", ".xls"]):
            return "excel"
        if "pdf" in q or ".pdf" in q:
            return "pdf"
        if any(k in q for k in ["ocr", "image", "screenshot", ".png", ".jpg", ".jpeg"]):
            return "vision"
        if any(k in q for k in ["search web", "search ", "open http", "open www", "browser"]):
            return "browser"
        if any(k in q for k in ["code", "python", "app", "script", "program", "build", "write file", "read file"]):
            return "coding"
        return "chat"

    def create_prompt(self, query: str, context: str = "") -> str:
        system = (
            "You are BADSHAH-AI, a helpful local desktop AI assistant. "
            "Reply in the user's language. Be practical, safe, and concise. "
            "For coding tasks, give working code and commands. "
            "Never claim you performed actions outside the local app unless a tool actually did it."
        )
        if context:
            return f"{system}\n\nRelevant memory:\n{context}\n\nUser request:\n{query}\n\nBADSHAH-AI:"
        return f"{system}\n\nUser request:\n{query}\n\nBADSHAH-AI:"
