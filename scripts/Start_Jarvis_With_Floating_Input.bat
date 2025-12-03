@echo off
echo ========================================
echo Starting Jarvis with Floating Input
echo ========================================
echo.

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Start floating input in new window
echo Starting floating input window...
start "Jarvis Floating Input" cmd /k python start_floating_input.py

REM Wait a moment
timeout /t 2 /nobreak >nul

REM Start Jarvis main
echo Starting Jarvis...
python Main.py

pause
