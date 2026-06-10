import importlib
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from badshah_ai.config.settings import settings, BASE_DIR

REQUIRED_MODULES = ["dotenv", "requests", "fastapi", "uvicorn", "rich", "streamlit", "pytest"]

def smoke_test():
    checks = []
    checks.append(("workspace", settings.safe_workspace.exists()))
    checks.append(("exports", settings.export_dir.exists()))
    checks.append(("memory_folder", settings.memory_db.parent.exists()))
    checks.append(("log_folder", settings.log_file.parent.exists()))
    missing = []
    for mod in REQUIRED_MODULES:
        try:
            importlib.import_module(mod)
        except Exception:
            missing.append(mod)
    checks.append(("required_modules", not missing))
    lines = [f"{name}: {'OK' if ok else 'FAIL'}" for name, ok in checks]
    if missing:
        lines.append("Missing modules: " + ", ".join(missing))
    return "\n".join(lines)

def run_all_tests():
    try:
        r = subprocess.run([sys.executable, "-m", "pytest", "-q"], cwd=str(BASE_DIR), capture_output=True, text=True, timeout=120)
        return (r.stdout + "\n" + r.stderr).strip()[:8000]
    except Exception as e:
        return "Test runner error: " + str(e)

def perf_check():
    start = time.perf_counter()
    from badshah_ai.core.brain import Brain
    brain = Brain()
    init_time = time.perf_counter() - start
    start2 = time.perf_counter()
    response = brain.run("version")
    run_time = time.perf_counter() - start2
    return f"Brain init: {init_time:.3f}s\nVersion command: {run_time:.3f}s\nResponse: {response}"

def dependency_audit():
    lines = []
    for mod in REQUIRED_MODULES:
        try:
            m = importlib.import_module(mod)
            version = getattr(m, "__version__", "installed")
            lines.append(f"{mod}: {version}")
        except Exception as e:
            lines.append(f"{mod}: MISSING ({e})")
    return "\n".join(lines)

def error_report():
    out = settings.export_dir / f"error_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    log_text = ""
    if settings.log_file.exists():
        log_text = settings.log_file.read_text(encoding="utf-8", errors="ignore")[-8000:]
    text = f'''BADSHAH-AI Error Report
Generated: {datetime.now().isoformat()}

Smoke Test:
{smoke_test()}

Dependency Audit:
{dependency_audit()}

Recent Logs:
{log_text}
'''
    out.write_text(text, encoding="utf-8")
    return f"Error report saved: {out}"

def bug_template():
    out = settings.export_dir / f"bug_report_template_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    text = '''# Bug Report

## Problem

## Steps to Reproduce
1.
2.
3.

## Expected Result

## Actual Result

## Screenshot / Logs

## System
- OS:
- Python:
- BADSHAH-AI Version:
'''
    out.write_text(text, encoding="utf-8")
    return f"Bug template saved: {out}"

def qa_checklist():
    return '''QA Checklist:
[ ] Installer works
[ ] CLI starts
[ ] Dashboard starts
[ ] test smoke passes
[ ] dependency audit reviewed
[ ] perf check acceptable
[ ] error report generated
[ ] GitHub push done
'''

if __name__ == "__main__":
    print(smoke_test())
