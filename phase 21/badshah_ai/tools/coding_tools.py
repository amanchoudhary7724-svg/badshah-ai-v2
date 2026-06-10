import subprocess
from datetime import datetime
from pathlib import Path
from badshah_ai.config.settings import BASE_DIR, settings
from badshah_ai.models.ollama_client import OllamaClient

CODE_EXTS = {".py", ".md", ".txt", ".bat", ".yml", ".yaml", ".json", ".toml", ".html", ".css", ".js"}

def code_scan(max_files=80):
    rows = []
    for p in BASE_DIR.rglob("*"):
        if any(part in {"venv", ".git", "__pycache__", "data"} for part in p.parts):
            continue
        if p.is_file() and p.suffix.lower() in CODE_EXTS:
            rows.append(str(p.relative_to(BASE_DIR)))
        if len(rows) >= max_files:
            break
    return "Code files:\n" + "\n".join(rows)

def read_code_file(path):
    p = (BASE_DIR / path).resolve()
    if not str(p).startswith(str(BASE_DIR.resolve())) or not p.exists():
        return "File not found or unsafe."
    if p.suffix.lower() not in CODE_EXTS:
        return "Unsupported file type."
    return p.read_text(encoding="utf-8", errors="ignore")[:12000]

def explain_code(path):
    content = read_code_file(path)
    if content.startswith("File not found") or content.startswith("Unsupported"):
        return content
    prompt = f"Explain this code clearly with purpose, important functions, and possible issues. File: {path}\n\n{content}"
    return OllamaClient().generate(prompt)

def code_patch(request):
    scan = code_scan(120)
    prompt = f'''You are BADSHAH-AI Coding Agent.
Create a SAFE patch proposal for this request:
{request}

Project files:
{scan}

Rules:
- Do not claim you modified files.
- Provide file paths and code blocks.
- Keep patch reviewable.
- Prefer workspace/patches or explain exact manual changes.
'''
    proposal = OllamaClient().generate(prompt)
    out = settings.export_dir / f"code_patch_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    out.write_text(proposal, encoding="utf-8")
    return f"Patch proposal saved: {out}"

def run_tests():
    try:
        r = subprocess.run(["python", "-m", "pytest", "-q"], cwd=str(BASE_DIR), capture_output=True, text=True, timeout=120)
        return (r.stdout + "\n" + r.stderr).strip()[:8000]
    except Exception as e:
        return "Test run error: " + str(e)

def open_vscode():
    try:
        subprocess.Popen(["code", str(BASE_DIR)], shell=False)
        return f"Opened VS Code: {BASE_DIR}"
    except Exception as e:
        return "VS Code open failed. Install VS Code CLI `code`. Error: " + str(e)
