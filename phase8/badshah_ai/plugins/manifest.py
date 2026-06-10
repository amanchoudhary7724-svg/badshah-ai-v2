PLUGINS = [
    {"name":"chat","description":"General LLM chat using Ollama"},
    {"name":"coding","description":"Code generation and workspace files"},
    {"name":"project","description":"Static website generator"},
    {"name":"pdf","description":"PDF text extraction"},
    {"name":"excel","description":"Excel/CSV summary"},
    {"name":"browser","description":"Open/search/scrape pages"},
    {"name":"vision","description":"OCR image text extraction"},
    {"name":"selfmod","description":"Safe self-mod proposal and sandbox apply"},
    {"name":"release","description":"Create release packages and status reports"},
]

def list_plugins():
    return PLUGINS
