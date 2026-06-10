PLUGINS = [
    {"name": "gmail_agent", "description": "Review-first Gmail/email draft workflow"},
    {"name": "calendar_agent", "description": "Review-first calendar event drafts"},
    {"name": "contacts", "description": "Local contact book"},
    {"name": "chat", "description": "Ollama chat"},
]
def list_plugins():
    return PLUGINS
