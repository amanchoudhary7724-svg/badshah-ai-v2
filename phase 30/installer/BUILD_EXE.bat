@echo off
title BADSHAH-AI EXE Builder
call venv\Scripts\activate
pip install pyinstaller
pyinstaller BADSHAH-AI.spec --clean --noconfirm
echo.
echo Build complete. Check dist\BADSHAH-AI\
pause
