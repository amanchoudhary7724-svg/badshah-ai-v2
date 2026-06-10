PLUGINS = [
    {"name": "multi_agent_planner", "description": "Plan, route and execute tasks across agents"},
    {"name": "chat", "description": "Ollama chat"},
    {"name": "advanced_memory", "description": "SQLite memory"},
    {"name": "workspace", "description": "Safe file tools"},
    {"name": "file_tools", "description": "PDF/Excel tools"},
    {"name": "browser", "description": "Open/search web"},
    {"name": "release", "description": "Export/release ZIP"},
]
def list_plugins(): return PLUGINS
