ALIASES = {
    "commands": "help",
    "about": "version",
    "release": "release package",
    "package": "release package",
    "env": "validate env",
}

class Planner:
    def normalize(self, q):
        return ALIASES.get(q.lower().strip(), q)

    def classify(self, q):
        x = self.normalize(q).lower().strip()
        if x in {"help","commands"}: return "help"
        if x == "suggest" or "suggest commands" in x: return "suggest"
        if x in {"version","about"}: return "version"
        if x == "status" or "project status" in x: return "status"
        if "validate env" in x: return "env"
        if x == "logs" or "show logs" in x: return "logs"
        if "smoke test" in x: return "smoke"
        if "changelog" in x: return "changelog"
        if "release package" in x: return "release"
        if "diagnostics" in x: return "diagnostics"
        if x == "config" or "show config" in x: return "config"
        if "plugins" in x: return "plugins"
        if "health" in x: return "health"
        if x.startswith("self modify") or x.startswith("self improve") or x.startswith("improve yourself"): return "selfmod"
        if "apply latest patch" in x or "apply patch" in x: return "apply_patch"
        if "show patches" in x or "list patches" in x: return "patches"
        if "backup workspace" in x or "backup" == x: return "backup"
        if "export" in x or "zip workspace" in x: return "export"
        if "tasks" in x or "task history" in x: return "tasks"
        if "scrape" in x: return "browser"
        if "create website" in x or "make website" in x: return "coding"
        if "pdf" in x or ".pdf" in x: return "pdf"
        if "excel" in x or ".xlsx" in x or ".csv" in x: return "excel"
        if "ocr" in x or "image" in x: return "vision"
        if "open app" in x: return "apps"
        if "search" in x or "open http" in x or x.startswith("open "): return "browser"
        if "email" in x: return "email"
        if "whatsapp" in x: return "whatsapp"
        if "code" in x or "write file" in x or "read file" in x: return "coding"
        return "chat"

    def prompt(self, q, ctx=""):
        return f"You are BADSHAH-AI. Reply in user's language.\nMemory:\n{ctx}\nUser:{q}\nAssistant:"
