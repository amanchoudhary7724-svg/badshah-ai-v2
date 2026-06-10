@echo off
title BADSHAH-AI API
call venv\Scripts\activate
uvicorn badshah_ai.api.server:app --reload
pause
