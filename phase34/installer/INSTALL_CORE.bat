@echo off
title BADSHAH-AI Core Installer
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements-core.txt
if not exist .env copy .env.example .env
python -m badshah_ai.tools.doctor
pause
