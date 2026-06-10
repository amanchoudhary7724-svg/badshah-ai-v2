from datetime import datetime
import re
from badshah_ai.config.settings import settings
from badshah_ai.models.ollama_client import OllamaClient
from badshah_ai.tools.export_tools import backup_workspace

PATCH_DIR = settings.safe_workspace / "patches"
SANDBOX_DIR = settings.safe_workspace / "sandbox_project"

def propose_self_modification(request: str) -> str:
    llm = OllamaClient()
    prompt = f'''
You are a senior Python engineer improving BADSHAH-AI.
Create a SAFE code improvement proposal for this request:

{request}

Output format:
# Patch Title
Short explanation.

## FILE: relative/path/file.py
```python
code here
```

Rules:
- Do not delete user data.
- Do not overwrite project files automatically.
- Keep changes small.
- Prefer files under sandbox_project/.
'''
    proposal = llm.generate(prompt)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    PATCH_DIR.mkdir(parents=True, exist_ok=True)
    target = PATCH_DIR / f"patch_{ts}.md"
    target.write_text(proposal, encoding="utf-8")
    return f"Self-modification proposal saved: {target}\nUse `apply latest patch` to apply generated FILE blocks into workspace/sandbox_project only."

def list_patches() -> str:
    PATCH_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(PATCH_DIR.glob("*.md"), reverse=True)
    if not files:
        return "No patches found."
    return "\n".join(str(p) for p in files[:20])

def _latest_patch():
    PATCH_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(PATCH_DIR.glob("*.md"), reverse=True)
    return files[0] if files else None

def apply_latest_patch() -> str:
    patch = _latest_patch()
    if not patch:
        return "No patch found."
    backup_msg = backup_workspace()
    text = patch.read_text(encoding="utf-8", errors="ignore")

    # Parse simple blocks:
    # ## FILE: some/path.py
    # ```python
    # code
    # ```
    pattern = re.compile(r"##\s*FILE:\s*(.+?)\n```(?:\w+)?\n(.*?)```", re.DOTALL | re.IGNORECASE)
    matches = pattern.findall(text)
    if not matches:
        return "No FILE blocks found in patch. Nothing applied. " + backup_msg

    applied = []
    SANDBOX_DIR.mkdir(parents=True, exist_ok=True)

    for rel, code in matches:
        rel = rel.strip().replace("\\", "/")
        rel = rel.lstrip("/").replace("..", "")
        target = (SANDBOX_DIR / rel).resolve()
        if not str(target).startswith(str(SANDBOX_DIR.resolve())):
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(code.strip() + "\n", encoding="utf-8")
        applied.append(str(target))

    if not applied:
        return "Patch blocked. No safe files applied. " + backup_msg

    return backup_msg + "\nApplied to sandbox only:\n" + "\n".join(applied)
