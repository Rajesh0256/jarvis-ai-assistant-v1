@echo off
title Jarvis AI Assistant - Installer
color 0B
cls

echo.
echo     ╔═══════════════════════════════════════════════════════╗
echo     ║                                                       ║
echo     ║        JARVIS AI ASSISTANT - INSTALLATION             ║
echo     ║                                                       ║
echo     ╚═══════════════════════════════════════════════════════╝
echo.
echo     This will set up Jarvis on your computer.
echo.
echo     Requirements:
echo     - Python 3.10 or higher
echo     - Internet connection
echo     - 2GB free disk space
echo.
echo     Press any key to start installation...
pause >nul

cls
echo.
echo     ╔═══════════════════════════════════════════════════════╗
echo     ║              INSTALLING JARVIS AI ASSISTANT           ║
echo     ╚═══════════════════════════════════════════════════════╝
echo.

cd /d "%~dp0"

echo     [1/4] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    color 0C
    echo.
    echo     [ERROR] Python not found!
    echo.
    echo     Please install Python 3.10 or higher from:
    echo     https://www.python.org/downloads/
    echo.
    echo     Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

python --version
echo     [✓] Python found!
echo.

echo     [2/4] Installing required packages...
echo     This may take 5-10 minutes, please wait...
echo.
pip install -r Requirements.txt
if errorlevel 1 (
    color 0C
    echo.
    echo     [ERROR] Failed to install packages!
    echo.
    echo     Please check your internet connection and try again.
    echo.
    pause
    exit /b 1
)
echo.
echo     [✓] Packages installed successfully!
echo.

echo     [3/4] Creating desktop shortcut...
(
echo Set oWS = WScript.CreateObject^("WScript.Shell"^)
echo sLinkFile = "%USERPROFILE%\Desktop\Jarvis AI Assistant.lnk"
echo Set oLink = oWS.CreateShortcut^(sLinkFile^)
echo oLink.TargetPath = "%CD%\Jarvis_Launcher.bat"
echo oLink.WorkingDirectory = "%CD%"
echo oLink.Description = "Jarvis AI Assistant - Your Personal AI"
echo oLink.Save
) > CreateShortcut.vbs

cscript //nologo CreateShortcut.vbs
del CreateShortcut.vbs
echo     [✓] Desktop shortcut created!
echo.

echo     [4/4] Finalizing installation...
timeout /t 2 /nobreak >nul
echo     [✓] Installation complete!
echo.

color 0A
cls
echo.
echo     ╔═══════════════════════════════════════════════════════╗
echo     ║                                                       ║
echo     ║          INSTALLATION COMPLETED SUCCESSFULLY!         ║
echo     ║                                                       ║
echo     ╚═══════════════════════════════════════════════════════╝
echo.
echo     ✓ Jarvis AI Assistant is now installed!
echo     ✓ Desktop shortcut created
echo.
echo     TO START JARVIS:
echo     - Double-click "Jarvis AI Assistant" on your desktop
echo     - Or run: Jarvis_Launcher.bat
echo.
echo     FEATURES:
echo     - Voice commands
echo     - File management
echo     - System control
echo     - Weather information
echo     - And much more!
echo.
echo     See COMMAND_EXAMPLES.md for all available commands.
echo.
echo     Press any key to launch Jarvis now...
pause >nul

start "" "%CD%\Jarvis_Launcher.bat"
