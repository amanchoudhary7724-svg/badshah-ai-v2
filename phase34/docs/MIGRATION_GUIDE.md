# Migration Guide

## Safe method

1. Backup current repo:
   ```bat
   scripts\backup_repo.bat
   ```

2. Extract latest ZIP into a new folder.

3. Copy your important custom files:
   - `.env`
   - `workspace/`
   - custom plugins
   - notes/docs

4. Install:
   ```bat
   installer\INSTALL_CORE.bat
   ```

5. Validate:
   ```text
   doctor
   repo validate
   migration checklist
   ```

6. Push:
   ```bash
   git add .
   git commit -m "BADSHAH-AI clean migration"
   git push origin main
   ```
