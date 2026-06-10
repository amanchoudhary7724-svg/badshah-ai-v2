AGENTS = [
    {"name": "planner", "skills": ["plan", "run plan"]},
    {"name": "llm_router", "skills": ["models", "ask fast/coding/smart"]},
    {"name": "memory", "skills": ["remember", "memory search"]},
    {"name": "plugin", "skills": ["plugin marketplace", "plugin enable"]},
    {"name": "communication", "skills": ["draft whatsapp", "draft email"]},
    {"name": "screen", "skills": ["screen shot", "screen ocr"]},
    {"name": "qa", "skills": ["test smoke", "qa checklist"]},
]
def list_agents():
    return AGENTS
