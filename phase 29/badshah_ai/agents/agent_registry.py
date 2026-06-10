AGENTS = [
    {"name": "qa", "skills": ["test smoke", "test all", "perf check", "dependency audit"]},
    {"name": "bugfix", "skills": ["error report", "bug template"]},
    {"name": "chat", "skills": ["general"]},
]
def list_agents():
    return AGENTS
