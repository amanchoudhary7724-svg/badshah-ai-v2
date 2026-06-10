# BADSHAH-AI v2 — Phase 34 Migration Helper

This phase is for safely moving from earlier phase ZIPs to one clean GitHub repo.

## Purpose
- Backup old repo
- Clean duplicate files
- Validate structure
- Create migration checklist
- Run final checks

## Commands

```text
migration guide
migration checklist
repo validate
doctor
version
```

## Recommended migration

```bat
scripts\backup_repo.bat
scripts\clean_temp.bat
installer\INSTALL_CORE.bat
scripts\test.bat
```

## GitHub Push

```bash
git add .
git commit -m "Add BADSHAH-AI v2 phase 34 migration helper"
git push origin main
```
