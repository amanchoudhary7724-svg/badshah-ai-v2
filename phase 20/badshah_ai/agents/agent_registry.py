AGENTS = [
    {"name": "chat", "skills": ["general", "answer", "reason"]},
    {"name": "memory", "skills": ["remember", "recall", "search memory"]},
    {"name": "workspace", "skills": ["write file", "read file", "create website"]},
    {"name": "file", "skills": ["pdf", "excel", "csv"]},
    {"name": "browser", "skills": ["search", "open url"]},
    {"name": "release", "skills": ["export workspace", "release package"]},
    {"name": "system", "skills": ["health", "safety", "system check"]},
]
def list_agents():
    return AGENTS
