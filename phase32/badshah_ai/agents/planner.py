import re

class MultiAgentPlanner:
    def make_plan(self, request):
        chunks = re.split(r"\s+(?:and|then|aur|phir)\s+", request.strip(), flags=re.I)
        return [{"agent": self.route(c), "task": c.strip()} for c in chunks if c.strip()] or [{"agent": "chat", "task": request}]

    def route(self, task):
        t = task.lower()
        if "plugin" in t or "custom note" in t: return "plugin"
        if "draft" in t or "contact" in t: return "communication"
        if "screen" in t or "ocr" in t: return "screen"
        if "test" in t or "qa" in t or "doctor" in t: return "qa"
        if "website" in t or "file" in t: return "workspace"
        return "chat"

    def format_plan(self, steps):
        return "\n".join(["Multi-Agent Plan:"] + [f"{i}. [{s['agent']}] {s['task']}" for i, s in enumerate(steps, 1)])
