from badshah_ai.config.settings import BASE_DIR, settings

def repo_tree():
    lines = []
    for name in ["badshah_ai", "installer", "scripts", "docs", "plugins", "tests"]:
        p = BASE_DIR / name
        lines.append(f"{name}/ -> {'OK' if p.exists() else 'MISSING'}")
    return "\n".join(lines)

def github_guide():
    path = BASE_DIR / "docs" / "GITHUB_UPLOAD_GUIDE.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return "Run: git add . && git commit -m \"BADSHAH-AI\" && git push origin main"

def release_notes():
    path = BASE_DIR / "docs" / "RELEASE_NOTES.md"
    return path.read_text(encoding="utf-8") if path.exists() else "No release notes."

def smoke_test():
    return "\n".join([
        f"workspace: {'OK' if settings.safe_workspace.exists() else 'FAIL'}",
        f"exports: {'OK' if settings.export_dir.exists() else 'FAIL'}",
        f"memory: {'OK' if settings.memory_db.parent.exists() else 'FAIL'}",
    ])
