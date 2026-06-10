# Final Release Guide

## 1. Install

```bat
installer\INSTALL_BADSHAH_AI.bat
```

## 2. Test

```bat
scripts\test.bat
```

Inside CLI:

```text
test smoke
qa checklist
version
```

## 3. Build EXE

```bat
installer\BUILD_EXE.bat
```

## 4. Run EXE

```bat
installer\RUN_EXE.bat
```

## 5. GitHub Release

Upload:
- `dist/BADSHAH-AI/`
- `badshah-ai-v2-phase30-final-exe-release.zip`

Tag:

```bash
git tag v3.0.0
git push origin v3.0.0
```
