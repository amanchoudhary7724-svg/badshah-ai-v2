@echo off
echo Cleaning temp/cache files...
rmdir /s /q __pycache__ 2>nul
rmdir /s /q .pytest_cache 2>nul
del /s /q *.pyc 2>nul
echo Done.
pause
