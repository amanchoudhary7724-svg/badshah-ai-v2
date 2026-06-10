@echo off
title BADSHAH-AI Setup
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
  echo Some voice packages may have failed. Try:
  echo pip install pipwin
  echo pipwin install pyaudio
)
if not exist .env copy .env.example .env
echo Setup complete.
pause
