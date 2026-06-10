PLUGINS = [
    {"name": "chat", "description": "Ollama chat"},
    {"name": "diagnostics", "description": "Health checks"},
    {"name": "project", "description": "Website generator"},
    {"name": "release", "description": "Release packaging"},
]
def list_plugins():
    return PLUGINS
