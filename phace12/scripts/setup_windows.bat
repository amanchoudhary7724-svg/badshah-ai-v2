@echo off
title BADSHAH-AI Setup
echo =====================================
echo BADSHAH-AI v1.2 Installer
echo =====================================
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
if not exist .env copy .env.example .env
echo.
echo Setup complete.
echo Next: ollama pull llama3.2:1b
echo Then run: scripts\run_cli.bat
pause
