PLUGINS = [
    {"name": "vscode_coding_agent", "description": "Repo scan, explain, patch proposal, tests, open VS Code"},
    {"name": "multi_agent_planner", "description": "Task plan and routing"},
    {"name": "chat", "description": "Ollama chat"},
    {"name": "memory", "description": "SQLite memory"},
    {"name": "workspace", "description": "Safe file tools"},
]
def list_plugins():
    return PLUGINS
