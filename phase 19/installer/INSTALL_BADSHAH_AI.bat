@echo off
title BADSHAH-AI Installer
echo BADSHAH-AI v1.9 Final Hardening Installer
python --version
if errorlevel 1 (
  echo Python not found. Install Python 3.10+ first.
  pause
  exit /b
)
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
if not exist .env copy .env.example .env
python -m badshah_ai.tools.system_check
echo Install complete.
pause
