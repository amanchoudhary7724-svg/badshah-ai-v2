# BADSHAH-AI v2 — Phase 30 Final EXE Release

Production release scaffold for Windows.

## Includes
- CLI app
- Desktop UI scaffold
- FastAPI server
- Streamlit dashboard
- QA tools
- EXE build scripts
- PyInstaller spec
- Final release checklist
- GitHub release guide

## Install Dev Version

```bat
installer\INSTALL_BADSHAH_AI.bat
```

## Build EXE

```bat
installer\BUILD_EXE.bat
```

Output:

```text
dist\BADSHAH-AI\BADSHAH-AI.exe
```

## Final Test

```bat
scripts\test.bat
```

## Push

```bash
git add .
git commit -m "Release BADSHAH-AI v2 phase 30 final exe release"
git push origin main
```
