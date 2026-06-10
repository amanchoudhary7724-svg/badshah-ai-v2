# BADSHAH-AI v2 — v1.5 Voice + Wake Word

Phase-15 adds voice assistant scaffold:

- Text-to-speech using `pyttsx3`
- Optional speech recognition using microphone
- Wake word loop scaffold: `badshah`
- Voice mode CLI
- Voice settings in `.env`
- Existing tools: memory, tasks, PDF, Excel, OCR, browser, app launcher, website generator

## Install

```bat
scripts\setup_windows.bat
```

## Run Normal CLI

```bat
scripts\run_cli.bat
```

## Run Voice Mode

```bat
scripts\run_voice.bat
```

## Voice Commands

Say:

```text
badshah help
badshah create website portfolio
badshah health check
badshah exit
```

## Notes

Speech recognition may need microphone permission. If it fails, normal CLI still works.

## Push

```bash
git add .
git commit -m "Add BADSHAH-AI v2 v1.5 voice wakeword"
git push origin main
```
