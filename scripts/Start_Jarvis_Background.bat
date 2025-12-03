@echo off
title Jarvis AI - Background Mode
color 0A
echo.
echo ============================================================
echo        JARVIS AI ASSISTANT - BACKGROUND MODE
echo ============================================================
echo.
echo Starting Jarvis in background mode...
echo.
echo Features:
echo  - Runs in system tray
echo  - Press Ctrl+Shift+J to activate
echo  - Always listening in background
echo  - Minimal resource usage
echo.
echo ============================================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed!
    echo Please install Python 3.10 from python.org
    pause
    exit /b 1
)

REM Run Jarvis in background mode
python Jarvis_Background.py

REM If script exits
echo.
echo Jarvis has stopped.
pause
