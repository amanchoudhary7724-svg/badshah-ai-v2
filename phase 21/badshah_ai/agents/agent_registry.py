AGENTS = [
    {"name": "coding", "skills": ["code scan", "code explain", "code patch", "test", "open vscode"]},
    {"name": "chat", "skills": ["general", "answer"]},
    {"name": "memory", "skills": ["remember", "recall"]},
    {"name": "workspace", "skills": ["write file", "read file", "create website"]},
    {"name": "release", "skills": ["release package"]},
]
def list_agents():
    return AGENTS
