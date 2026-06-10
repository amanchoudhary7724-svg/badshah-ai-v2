@echo off
title BADSHAH-AI Installer
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
if not exist .env copy .env.example .env
echo Install complete.
echo Recommended:
echo ollama pull llama3.2:1b
echo ollama pull qwen2.5-coder:1.5b
pause
