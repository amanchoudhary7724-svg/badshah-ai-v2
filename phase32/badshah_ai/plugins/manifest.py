PLUGINS = [
    {"name": "real_run_fix_pack", "description": "First-run diagnostics and safer install"},
    {"name": "llm_router", "description": "Ollama multi-model routing"},
    {"name": "plugin_marketplace", "description": "Dynamic plugins"},
    {"name": "qa_tools", "description": "Smoke tests and doctor"},
]
def list_plugins():
    return PLUGINS
