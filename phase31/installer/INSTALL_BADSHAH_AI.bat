@echo off
title BADSHAH-AI Installer
echo Installing BADSHAH-AI v3.1 Integrated Repo...
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
if not exist .env copy .env.example .env
echo.
echo Install complete.
echo Recommended: ollama pull llama3.2:1b
pause
