from datetime import datetime
import re
from badshah_ai.config.settings import settings
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.tools.export_tools import backup_workspace

PATCH_DIR = settings.safe_workspace / "patches"
SANDBOX_DIR = settings.safe_workspace / "sandbox_project"

def propose_self_modification(request: str) -> str:
    prompt = f'''Create SAFE code improvement proposal for BADSHAH-AI request: {request}
Output format:
## FILE: relative/path/file.py
```python
code here
```
Do not overwrite project files.'''
    proposal = OllamaClient().generate(prompt)
    PATCH_DIR.mkdir(parents=True, exist_ok=True)
    target = PATCH_DIR / f"patch_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    target.write_text(proposal, encoding="utf-8")
    return f"Self-modification proposal saved: {target}"

def list_patches():
    PATCH_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(PATCH_DIR.glob("*.md"), reverse=True)
    return "\n".join(str(p) for p in files[:20]) if files else "No patches found."

def apply_latest_patch():
    files = sorted(PATCH_DIR.glob("*.md"), reverse=True)
    if not files:
        return "No patch found."
    backup = backup_workspace()
    text = files[0].read_text(encoding="utf-8", errors="ignore")
    matches = re.findall(r"##\s*FILE:\s*(.+?)\n```(?:\w+)?\n(.*?)```", text, re.S | re.I)
    if not matches:
        return "No FILE blocks found. " + backup
    applied = []
    SANDBOX_DIR.mkdir(parents=True, exist_ok=True)
    for rel, code in matches:
        rel = rel.strip().replace("\\","/").lstrip("/").replace("..","")
        target = (SANDBOX_DIR / rel).resolve()
        if str(target).startswith(str(SANDBOX_DIR.resolve())):
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(code.strip()+"\n", encoding="utf-8")
            applied.append(str(target))
    return backup + "\nApplied to sandbox:\n" + "\n".join(applied)
