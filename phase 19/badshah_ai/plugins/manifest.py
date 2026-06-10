PLUGINS = [
    {"name": "chat", "description": "Ollama chat"},
    {"name": "advanced_memory", "description": "SQLite + optional ChromaDB semantic memory"},
    {"name": "voice", "description": "TTS + speech recognition"},
    {"name": "browser_automation", "description": "Playwright title/text/screenshot"},
    {"name": "safety", "description": "Safety policy and diagnostics"},
    {"name": "workspace", "description": "Safe file tools"},
    {"name": "release", "description": "Export/release ZIP"},
]
def list_plugins(): return PLUGINS
