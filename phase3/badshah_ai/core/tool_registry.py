class ToolRegistry:
    def __init__(self) -> None:
        self.tools = {}

    def register(self, name: str, description: str, fn) -> None:
        self.tools[name] = {"description": description, "fn": fn}

    def list_tools(self) -> list[dict]:
        return [{"name": name, "description": meta["description"]} for name, meta in self.tools.items()]

    def run(self, name: str, *args, **kwargs):
        if name not in self.tools:
            raise KeyError(f"Tool not found: {name}")
        return self.tools[name]["fn"](*args, **kwargs)
