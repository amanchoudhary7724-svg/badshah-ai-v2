import re
from badshah_ai.agents.base import BaseAgent
from badshah_ai.tools.file_tools import write_text_file

class EmailAgent(BaseAgent):
    name = "email"

    def handle(self, query: str) -> str:
        # Safe Phase 3: creates draft text file, does not send email.
        email_match = re.search(r'[\w\.-]+@[\w\.-]+', query)
        to = email_match.group(0) if email_match else "recipient@example.com"
        subject = "Draft from BADSHAH-AI"
        body = query
        content = f"To: {to}\nSubject: {subject}\n\n{body}\n"
        return write_text_file("drafts/email_draft.txt", content)
