PLUGINS = [
    {"name": "integrated_core", "description": "Single integrated BADSHAH-AI repo"},
    {"name": "llm_router", "description": "Ollama multi-model routing"},
    {"name": "multi_agent_planner", "description": "Task planning"},
    {"name": "plugin_marketplace", "description": "Dynamic plugins"},
    {"name": "communication_drafts", "description": "Review-first drafts"},
    {"name": "screen_vision", "description": "Screenshot/OCR scaffold"},
    {"name": "qa_tools", "description": "Smoke tests and QA checklist"},
]
def list_plugins():
    return PLUGINS
