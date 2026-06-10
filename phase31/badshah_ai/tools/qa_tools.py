import time
from datetime import datetime
from badshah_ai.config.settings import settings
def smoke_test():
    return "\n".join([
        f"workspace: {'OK' if settings.safe_workspace.exists() else 'FAIL'}",
        f"exports: {'OK' if settings.export_dir.exists() else 'FAIL'}",
        f"memory: {'OK' if settings.memory_db.parent.exists() else 'FAIL'}",
    ])
def perf_check():
    start = time.perf_counter()
    from badshah_ai.core.brain import Brain
    Brain()
    return f"Brain init: {time.perf_counter()-start:.3f}s"
def qa_checklist():
    return "[ ] install\n[ ] cli\n[ ] dashboard\n[ ] smoke\n[ ] ollama\n[ ] github push"
def error_report():
    out = settings.export_dir / f"error_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    out.write_text(smoke_test(), encoding="utf-8")
    return f"Error report saved: {out}"
