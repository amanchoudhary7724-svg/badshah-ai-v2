PLUGINS = [
    {"name": "qa_testing", "description": "Smoke tests, dependency audit, performance check"},
    {"name": "bug_reporter", "description": "Error report and bug template export"},
    {"name": "chat", "description": "Ollama chat"},
]
def list_plugins():
    return PLUGINS
