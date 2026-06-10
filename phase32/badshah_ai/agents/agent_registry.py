AGENTS = [
    {"name": "doctor", "skills": ["doctor", "test smoke"]},
    {"name": "planner", "skills": ["plan", "run plan"]},
    {"name": "llm_router", "skills": ["models", "ask"]},
    {"name": "plugin", "skills": ["plugin marketplace"]},
]
def list_agents():
    return AGENTS
