PLUGINS = [
    {"name": "chat", "description": "General LLM chat using Ollama"},
    {"name": "coding", "description": "Code generation and safe workspace file writing"},
    {"name": "project", "description": "Static website generator"},
    {"name": "pdf", "description": "PDF text extraction"},
    {"name": "excel", "description": "Excel/CSV summary"},
    {"name": "browser", "description": "Open/search/scrape web pages"},
    {"name": "vision", "description": "OCR image text extraction"},
    {"name": "apps", "description": "Safe whitelisted Windows app launcher"},
    {"name": "draft", "description": "Email/WhatsApp draft writer"},
    {"name": "selfmod", "description": "Safe self-modification proposal and sandbox apply"},
    {"name": "export", "description": "Backup/export workspace"},
    {"name": "diagnostics", "description": "Health, config and command help"},
]

def list_plugins():
    return PLUGINS
