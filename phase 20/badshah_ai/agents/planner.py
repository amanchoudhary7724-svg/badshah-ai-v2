import re
from badshah_ai.agents.agent_registry import list_agents

class MultiAgentPlanner:
    def list_agents_text(self):
        return "\n".join([f"- {a['name']}: {', '.join(a['skills'])}" for a in list_agents()])

    def make_plan(self, request: str):
        text = request.strip()
        chunks = re.split(r"\s+(?:and|then|aur|phir)\s+", text, flags=re.I)
        steps = []
        for chunk in chunks:
            c = chunk.strip()
            if not c:
                continue
            agent = self.route_agent(c)
            steps.append({"agent": agent, "task": c})
        if not steps:
            steps.append({"agent": "chat", "task": request})
        return steps

    def route_agent(self, task: str):
        t = task.lower()
        if t.startswith("remember") or "memory" in t:
            return "memory"
        if "website" in t or "write file" in t or "read file" in t:
            return "workspace"
        if ".pdf" in t or ".xlsx" in t or ".csv" in t or "excel" in t or "pdf" in t:
            return "file"
        if t.startswith("search") or t.startswith("open "):
            return "browser"
        if "release" in t or "export" in t:
            return "release"
        if "health" in t or "system" in t or "safety" in t:
            return "system"
        return "chat"

    def format_plan(self, steps):
        lines = ["Multi-Agent Plan:"]
        for i, s in enumerate(steps, 1):
            lines.append(f"{i}. [{s['agent']}] {s['task']}")
        return "\n".join(lines)
