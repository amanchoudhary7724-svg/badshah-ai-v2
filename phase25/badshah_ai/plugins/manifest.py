PLUGINS = [
    {"name": "llm_router", "description": "Multi-model local Ollama routing"},
    {"name": "fallback_model", "description": "Fallback model when selected model fails"},
    {"name": "chat", "description": "General AI chat"},
]
def list_plugins():
    return PLUGINS
