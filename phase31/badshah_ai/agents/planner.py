import re

class MultiAgentPlanner:
    def make_plan(self, request):
        chunks = re.split(r"\s+(?:and|then|aur|phir)\s+", request.strip(), flags=re.I)
        steps = []
        for chunk in chunks:
            if chunk.strip():
                steps.append({"agent": self.route(chunk), "task": chunk.strip()})
        return steps or [{"agent": "chat", "task": request}]

    def route(self, task):
        t = task.lower()
        if t.startswith("remember") or "memory" in t:
            return "memory"
        if "plugin" in t or "custom note" in t:
            return "plugin"
        if "draft" in t or "contact" in t:
            return "communication"
        if "screen" in t or "ocr" in t:
            return "screen"
        if "test" in t or "qa" in t:
            return "qa"
        if "model" in t or t.startswith("ask "):
            return "llm_router"
        if "website" in t or "workspace" in t:
            return "workspace"
        return "chat"

    def format_plan(self, steps):
        return "\n".join(["Multi-Agent Plan:"] + [f"{i}. [{s['agent']}] {s['task']}" for i, s in enumerate(steps, 1)])
