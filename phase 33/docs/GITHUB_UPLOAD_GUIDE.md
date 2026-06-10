# GitHub Upload Guide

## Clean replace method

1. Extract this ZIP.
2. Copy all files into your GitHub repo folder.
3. Run:

```bash
git status
git add .
git commit -m "BADSHAH-AI v3.3 clean release"
git push origin main
```

## If Git asks for login
Use GitHub Desktop or GitHub token.

## Important
Do not upload:
- `venv/`
- `.env`
- `data/memory/*.sqlite3`
- `logs/*.log`
