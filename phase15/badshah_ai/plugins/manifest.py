PLUGINS = [
    {"name": "chat", "description": "Ollama chat"},
    {"name": "voice", "description": "TTS + speech recognition + wake word scaffold"},
    {"name": "memory", "description": "SQLite memory"},
    {"name": "tasks", "description": "Task history"},
    {"name": "workspace", "description": "Safe file tools"},
    {"name": "project", "description": "Website generator"},
    {"name": "pdf", "description": "PDF extraction"},
    {"name": "excel", "description": "Excel/CSV summary"},
    {"name": "ocr", "description": "Image OCR"},
    {"name": "browser", "description": "Open/search web"},
    {"name": "apps", "description": "Safe app launcher"},
    {"name": "release", "description": "Export/release ZIP"},
]
def list_plugins():
    return PLUGINS
