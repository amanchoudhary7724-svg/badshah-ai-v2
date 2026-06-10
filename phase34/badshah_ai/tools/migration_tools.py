from badshah_ai.config.settings import BASE_DIR

REQUIRED = [
    "badshah_ai",
    "installer",
    "scripts",
    "docs",
    "tests",
    "requirements-core.txt",
    ".env.example",
    "README.md",
]

def repo_validate():
    lines = []
    ok = True
    for item in REQUIRED:
        exists = (BASE_DIR / item).exists()
        ok = ok and exists
        lines.append(f"{item}: {'OK' if exists else 'MISSING'}")
    lines.append("")
    lines.append("Repo status: " + ("OK" if ok else "CHECK REQUIRED"))
    return "\n".join(lines)

def migration_guide():
    p = BASE_DIR / "docs" / "MIGRATION_GUIDE.md"
    return p.read_text(encoding="utf-8") if p.exists() else "Migration guide missing."

def migration_checklist():
    p = BASE_DIR / "docs" / "MIGRATION_CHECKLIST.md"
    return p.read_text(encoding="utf-8") if p.exists() else "Migration checklist missing."
