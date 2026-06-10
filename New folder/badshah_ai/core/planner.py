class Planner:
    def create_prompt(self, query: str, context: str = "") -> str:
        system = (
            "You are BADSHAH-AI, a helpful local desktop AI assistant. "
            "Reply in the user's language. Be practical, safe, and concise. "
            "For coding tasks, give working code and commands. "
            "Never claim you performed actions outside the local app unless a tool actually did it."
        )
        if context:
            return f"{system}\n\nRelevant memory:\n{context}\n\nUser request:\n{query}\n\nBADSHAH-AI:"
        return f"{system}\n\nUser request:\n{query}\n\nBADSHAH-AI:"
