@echo off
title BADSHAH-AI Setup
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
if not exist .env copy .env.example .env
echo Setup complete.
echo For browser automation run: scripts\install_browser.bat
pause
