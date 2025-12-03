@echo off
echo ========================================
echo SIMPLE JARVIS BUILD
echo ========================================
echo.

REM Activate venv
call .venv\Scripts\activate.bat

echo Cleaning old builds...
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build

echo.
echo Building Jarvis (this takes 5-10 minutes)...
echo Please wait...
echo.

pyinstaller --clean --onedir --windowed --name Jarvis_AI ^
    --add-data "Frontend;Frontend" ^
    --add-data "Backend;Backend" ^
    --add-data ".env;." ^
    --hidden-import PyQt5 ^
    --hidden-import groq ^
    --hidden-import google.generativeai ^
    Main.py

echo.
if exist "dist\Jarvis_AI\Jarvis_AI.exe" (
    echo ✅ SUCCESS! Executable created!
    echo.
    echo Location: dist\Jarvis_AI\Jarvis_AI.exe
    echo.
    echo Creating Data folder...
    mkdir dist\Jarvis_AI\Data 2>nul
    
    echo Creating portable ZIP...
    powershell -Command "Compress-Archive -Path 'dist\Jarvis_AI' -DestinationPath 'Jarvis_AI_Portable.zip' -Force"
    
    echo.
    echo ✅ DONE!
    echo Portable ZIP: Jarvis_AI_Portable.zip
    echo.
) else (
    echo ❌ Build failed!
    echo.
)

pause
