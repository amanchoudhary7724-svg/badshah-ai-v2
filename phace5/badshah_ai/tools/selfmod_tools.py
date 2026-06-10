from datetime import datetime
from pathlib import Path
from badshah_ai.config.settings import settings
from badshah_ai.models.ollama_client import OllamaClient

PATCH_DIR = "patches"

def propose_self_modification(request: str) -> str:
    llm = OllamaClient()
    prompt = f'''
You are a senior Python engineer improving BADSHAH-AI.
Create a SAFE code improvement proposal for this request:

{request}

Rules:
- Do not delete user data.
- Do not overwrite files automatically.
- Provide file paths and code blocks.
- Keep changes small and reviewable.
- Mention test command.
'''
    proposal = llm.generate(prompt)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{PATCH_DIR}/patch_{ts}.md"
    target = (settings.safe_workspace / filename).resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(proposal, encoding="utf-8")
    return f"Self-modification proposal saved: {target}\nReview this file before applying changes."

def list_patches() -> str:
    patch_root = settings.safe_workspace / PATCH_DIR
    patch_root.mkdir(parents=True, exist_ok=True)
    files = sorted(patch_root.glob("*.md"), reverse=True)
    if not files:
        return "No patches found."
    return "\n".join(str(p) for p in files[:20])
