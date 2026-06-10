from badshah_ai.core.planner import Planner
from badshah_ai.agents.agents import SimpleAgent, help_fn, config_fn, plugins_fn, tasks_fn, coding_fn, browser_fn, pdf_fn, excel_fn, vision_fn, app_fn, draft_fn
from badshah_ai.tools.export_tools import export_workspace, backup_workspace, release_package
from badshah_ai.tools.status_tools import version, changelog, status_report, command_suggestions, show_logs
from badshah_ai.tools.health_tools import health_check, diagnostics, validate_env, smoke_test
from badshah_ai.tools.selfmod_tools import propose_self_modification, list_patches, apply_latest_patch

class Router:
    def __init__(self):
        self.planner = Planner()
        self.map = {
            "help": SimpleAgent("help", help_fn),
            "suggest": SimpleAgent("suggest", lambda q: command_suggestions()),
            "version": SimpleAgent("version", lambda q: version()),
            "status": SimpleAgent("status", lambda q: status_report()),
            "env": SimpleAgent("env", lambda q: validate_env()),
            "logs": SimpleAgent("logs", lambda q: show_logs()),
            "smoke": SimpleAgent("smoke", lambda q: smoke_test()),
            "changelog": SimpleAgent("changelog", lambda q: changelog()),
            "release": SimpleAgent("release", lambda q: release_package()),
            "config": SimpleAgent("config", config_fn),
            "plugins": SimpleAgent("plugins", plugins_fn),
            "diagnostics": SimpleAgent("diagnostics", lambda q: diagnostics()),
            "health": SimpleAgent("health", lambda q: health_check()),
            "selfmod": SimpleAgent("selfmod", propose_self_modification),
            "apply_patch": SimpleAgent("apply_patch", lambda q: apply_latest_patch()),
            "patches": SimpleAgent("patches", lambda q: list_patches()),
            "backup": SimpleAgent("backup", lambda q: backup_workspace()),
            "coding": SimpleAgent("coding", coding_fn),
            "export": SimpleAgent("export", lambda q: export_workspace()),
            "tasks": SimpleAgent("tasks", tasks_fn),
            "browser": SimpleAgent("browser", browser_fn),
            "pdf": SimpleAgent("pdf", pdf_fn),
            "excel": SimpleAgent("excel", excel_fn),
            "vision": SimpleAgent("vision", vision_fn),
            "apps": SimpleAgent("apps", app_fn),
            "email": SimpleAgent("draft", draft_fn),
            "whatsapp": SimpleAgent("draft", draft_fn),
        }

    def route(self, q):
        return self.map.get(self.planner.classify(q))
