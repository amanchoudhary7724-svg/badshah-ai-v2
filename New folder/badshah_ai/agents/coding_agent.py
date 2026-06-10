from badshah_ai.agents.base import BaseAgent
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.tools.file_tools import write_text_file, read_text_file

class CodingAgent(BaseAgent):
    name = "coding"

    def __init__(self) -> None:
        self.llm = OllamaClient()

    def handle(self, query: str) -> str:
        q = query.lower()

        if q.startswith("write file "):
            # Format: write file filename.ext content here
            parts = query.split(" ", 3)
            if len(parts) < 4:
                return "Use format: write file filename.txt content"
            _, _, filename, content = parts
            return write_text_file(filename, content)

        if q.startswith("read file "):
            filename = query.split(" ", 2)[2]
            return read_text_file(filename)

        prompt = (
            "You are BADSHAH Coding Agent. Generate clean, runnable, secure code. "
            "Include file names and run commands when useful. User request:\n" + query
        )
        return self.llm.generate(prompt)
