class Planner:
    def classify(self, q):
        x = q.lower()
        if "health" in x: return "health"
        if x.startswith("self modify") or x.startswith("self improve") or x.startswith("improve yourself"): return "selfmod"
        if "show patches" in x or "list patches" in x: return "patches"
        if "export" in x or "zip workspace" in x: return "export"
        if "tasks" in x or "task history" in x: return "tasks"
        if "scrape" in x: return "browser"
        if "create website" in x or "make website" in x: return "coding"
        if "pdf" in x or ".pdf" in x: return "pdf"
        if "excel" in x or ".xlsx" in x or ".csv" in x: return "excel"
        if "ocr" in x or "image" in x: return "vision"
        if "open app" in x: return "apps"
        if "search" in x or "open http" in x: return "browser"
        if "email" in x: return "email"
        if "whatsapp" in x: return "whatsapp"
        if "code" in x or "write file" in x or "read file" in x: return "coding"
        return "chat"

    def prompt(self, q, ctx=""):
        return f"You are BADSHAH-AI. Reply in user's language.\nMemory:\n{ctx}\nUser:{q}\nAssistant:"
