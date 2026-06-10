AGENTS = [
    {"name": "release", "skills": ["build exe", "release package", "qa checklist"]},
    {"name": "qa", "skills": ["test smoke", "perf check", "error report"]},
    {"name": "chat", "skills": ["general"]},
]
def list_agents():
    return AGENTS
