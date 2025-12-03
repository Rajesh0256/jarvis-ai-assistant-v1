@echo off
title Jarvis AI Assistant
color 0A
cls

echo.
echo     ╔═══════════════════════════════════════════════════════╗
echo     ║                                                       ║
echo     ║           J A R V I S   A I   A S S I S T A N T       ║
echo     ║                                                       ║
echo     ║                      Version 1.0                      ║
echo     ║                                                       ║
echo     ╚═══════════════════════════════════════════════════════╝
echo.
echo     [*] Initializing Jarvis...
echo.

cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    color 0C
    echo.
    echo     ╔═══════════════════════════════════════════════════════╗
    echo     ║                    ERROR: Python Not Found            ║
    echo     ╚═══════════════════════════════════════════════════════╝
    echo.
    echo     Python is not installed or not in PATH.
    echo.
    echo     Please install Python 3.10 or higher from:
    echo     https://www.python.org/downloads/
    echo.
    echo     Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

echo     [*] Python detected...
echo     [*] Checking virtual environment...

REM Try to activate virtual environment if it exists
if exist ".venv\Scripts\activate.bat" (
    echo     [*] Activating virtual environment...
    call .venv\Scripts\activate.bat
)

echo     [*] Starting Jarvis AI Assistant...
echo.
echo     ═══════════════════════════════════════════════════════
echo.

REM Start Jarvis
python Main.py

REM Check if Jarvis exited with error
if errorlevel 1 (
    color 0C
    echo.
    echo     ═══════════════════════════════════════════════════════
    echo.
    echo     [!] Jarvis encountered an error!
    echo.
    echo     Common solutions:
    echo     1. Run: pip install -r Requirements.txt
    echo     2. Check if all files are present
    echo     3. See TROUBLESHOOTING.md for help
    echo.
    echo     ═══════════════════════════════════════════════════════
    echo.
)

pause
