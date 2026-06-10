# Voice Setup

## Install
Run:

```bat
scripts\setup_windows.bat
```

If PyAudio fails:

```bat
pip install pipwin
pipwin install pyaudio
```

## Run Voice Mode

```bat
scripts\run_voice.bat
```

## Wake Word

Default wake word:

```text
badshah
```

Change in `.env`:

```env
WAKE_WORD=badshah
```
