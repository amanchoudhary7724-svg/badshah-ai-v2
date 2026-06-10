PLUGINS = [
    {"name": "migration_helper", "description": "Backup, validate, and migrate old phase repos"},
    {"name": "doctor", "description": "First-run diagnostics"},
    {"name": "ollama_chat", "description": "Basic Ollama chat"},
]
def list_plugins():
    return PLUGINS
