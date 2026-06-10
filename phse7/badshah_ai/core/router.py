from badshah_ai.core.planner import Planner
from badshah_ai.agents.agents import (
    HelpAgent, ConfigAgent, PluginAgent, DiagnosticsAgent, HealthAgent,
    SelfModAgent, ApplyPatchAgent, PatchListAgent, BackupAgent,
    CodingAgent, ExportAgent, TaskAgent, BrowserAgent, PDFAgent, ExcelAgent,
    VisionAgent, AppAgent, DraftAgent
)

class Router:
    def __init__(self):
        self.planner = Planner()
        self.map = {
            "help": HelpAgent(),
            "config": ConfigAgent(),
            "plugins": PluginAgent(),
            "diagnostics": DiagnosticsAgent(),
            "health": HealthAgent(),
            "selfmod": SelfModAgent(),
            "apply_patch": ApplyPatchAgent(),
            "patches": PatchListAgent(),
            "backup": BackupAgent(),
            "coding": CodingAgent(),
            "export": ExportAgent(),
            "tasks": TaskAgent(),
            "browser": BrowserAgent(),
            "pdf": PDFAgent(),
            "excel": ExcelAgent(),
            "vision": VisionAgent(),
            "apps": AppAgent(),
            "email": DraftAgent(),
            "whatsapp": DraftAgent(),
        }

    def route(self,q):
        return self.map.get(self.planner.classify(q))
