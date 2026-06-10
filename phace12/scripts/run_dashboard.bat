@echo off
title BADSHAH-AI Dashboard
call venv\Scripts\activate
streamlit run badshah_ai/dashboard/app.py
pause
