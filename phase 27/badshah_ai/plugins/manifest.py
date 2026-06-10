PLUGINS = [
    {"name": "plugin_marketplace", "description": "Dynamic local plugin loading"},
    {"name": "sample_custom_notes", "description": "Sample plugin included"},
    {"name": "pyqt_desktop_ui", "description": "Desktop interface"},
    {"name": "llm_router", "description": "Multi-model local Ollama routing"},
]
def list_plugins():
    return PLUGINS
