from pathlib import Path
from datetime import datetime
from badshah_ai.config.settings import settings, BASE_DIR

SAFETY_TEXT = '''Safety Policy:
- Workspace-only file writes
- Destructive actions blocked by default
- No auto payment/password extraction
- No auto email/WhatsApp sending
- Self-modification must be review-first
'''

def safety_policy():
    return SAFETY_TEXT

def system_check():
    checks = [
        f"Workspace exists: {settings.safe_workspace.exists()}",
        f"Exports exists: {settings.export_dir.exists()}",
        f"Memory folder exists: {settings.memory_db.parent.exists()}",
        f"Destructive actions allowed: {settings.allow_destructive_actions}",
    ]
    return "\n".join(checks)

def diagnostics_report():
    out = settings.export_dir / f"diagnostics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    text = SAFETY_TEXT + "\n" + system_check()
    out.write_text(text, encoding="utf-8")
    return f"Diagnostics report saved: {out}"

def backup_config():
    env = BASE_DIR / ".env"
    if not env.exists():
        return ".env not found"
    backup = BASE_DIR / ".env.backup"
    backup.write_text(env.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
    return f"Config backup saved: {backup}"

def restore_config():
    env = BASE_DIR / ".env"
    backup = BASE_DIR / ".env.backup"
    if not backup.exists():
        return ".env.backup not found"
    env.write_text(backup.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
    return "Config restored from .env.backup"
