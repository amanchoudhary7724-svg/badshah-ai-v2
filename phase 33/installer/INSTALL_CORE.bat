@echo off
title BADSHAH-AI Core Installer
python --version
if errorlevel 1 (
  echo Python missing. Install Python 3.10+ first.
  pause
  exit /b
)
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements-core.txt
if not exist .env copy .env.example .env
python -m badshah_ai.tools.doctor
pause
