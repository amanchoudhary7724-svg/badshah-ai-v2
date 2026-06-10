import subprocess
import zipfile
from datetime import datetime
from pathlib import Path
from badshah_ai.config.settings import BASE_DIR, settings

def _run(cmd):
    try:
        r = subprocess.run(cmd, cwd=str(BASE_DIR), capture_output=True, text=True, timeout=120)
        return (r.stdout + "\n" + r.stderr).strip()
    except Exception as e:
        return "Command error: " + str(e)

def update_status():
    git_dir = BASE_DIR / ".git"
    if not git_dir.exists():
        return "This folder is not a Git repo. Use github push guide."
    return _run(["git", "status", "--short"]) or "Working tree clean."

def update_backup():
    out = settings.export_dir / f"pre_update_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in BASE_DIR.rglob("*"):
            if p.is_file() and "venv" not in p.parts and ".git" not in p.parts and "__pycache__" not in p.parts:
                z.write(p, p.relative_to(BASE_DIR))
    return f"Backup created: {out}"

def update_pull():
    if not (BASE_DIR / ".git").exists():
        return "Not a Git repo. Cannot pull."
    status = update_status()
    if status != "Working tree clean.":
        return "Working tree has changes. Run update backup and commit/stash before pull.\n\n" + status
    return _run(["git", "pull"])

def release_notes():
    out = settings.export_dir / f"release_notes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    text = f'''# BADSHAH-AI Release Notes

Version: 2.8.0

## Highlights
- Self-updater scaffold
- Git status check
- Backup before update
- Git pull helper
- Release notes generator

## Safe Update Flow
1. update status
2. update backup
3. update pull
'''
    out.write_text(text, encoding="utf-8")
    return f"Release notes saved: {out}"

def github_push_guide():
    return f'''GitHub Push Guide:

Repo:
{settings.github_repo_url}

Commands:
git add .
git commit -m "Update BADSHAH-AI"
git push origin main
'''
