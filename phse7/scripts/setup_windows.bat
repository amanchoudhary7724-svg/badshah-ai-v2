@echo off
echo Setting up BADSHAH-AI v2 Phase 7...
python -m venv venv
call venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
if not exist .env copy .env.example .env
echo Setup complete.
pause
