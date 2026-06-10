import importlib
import time
from datetime import datetime
from badshah_ai.config.settings import settings

REQUIRED_MODULES = ["dotenv", "requests", "rich"]

def smoke_test():
    checks = [
        ("workspace", settings.safe_workspace.exists()),
        ("exports", settings.export_dir.exists()),
        ("memory_folder", settings.memory_db.parent.exists()),
        ("log_folder", settings.log_file.parent.exists()),
    ]
    lines = [f"{name}: {'OK' if ok else 'FAIL'}" for name, ok in checks]
    for mod in REQUIRED_MODULES:
        try:
            importlib.import_module(mod)
            lines.append(f"{mod}: OK")
        except Exception:
            lines.append(f"{mod}: FAIL")
    return "\n".join(lines)

def perf_check():
    start = time.perf_counter()
    from badshah_ai.core.brain import Brain
    brain = Brain()
    init_time = time.perf_counter() - start
    return f"Brain init: {init_time:.3f}s"

def error_report():
    out = settings.export_dir / f"final_error_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    text = "BADSHAH-AI Final Error Report\n\n" + smoke_test()
    out.write_text(text, encoding="utf-8")
    return f"Error report saved: {out}"

def qa_checklist():
    return '''Final QA Checklist:
[ ] Install works
[ ] CLI starts
[ ] test smoke OK
[ ] EXE builds
[ ] EXE starts
[ ] Ollama model available
[ ] GitHub release uploaded
'''
