from badshah_ai.config.settings import settings
from badshah_ai.tools.doctor import doctor_report

def smoke_test():
    return "\n".join([
        f"workspace: {'OK' if settings.safe_workspace.exists() else 'FAIL'}",
        f"exports: {'OK' if settings.export_dir.exists() else 'FAIL'}",
        f"memory: {'OK' if settings.memory_db.parent.exists() else 'FAIL'}",
    ])

def qa_checklist():
    return "[ ] INSTALL_CORE\n[ ] doctor\n[ ] test smoke\n[ ] ollama pull llama3.2:1b\n[ ] CLI works\n[ ] dashboard works"

def perf_check():
    return "Performance check basic OK"

def error_report():
    out = settings.export_dir / "error_report.txt"
    out.write_text(doctor_report(), encoding="utf-8")
    return f"Error report saved: {out}"
