from badshah_ai.config.settings import settings
def safety_policy():
    return "Safety: workspace-only writes, destructive actions blocked, browser actions limited."
def system_check():
    return "\n".join([
        f"Workspace exists: {settings.safe_workspace.exists()}",
        f"Exports exists: {settings.export_dir.exists()}",
        f"Destructive allowed: {settings.allow_destructive_actions}",
    ])
