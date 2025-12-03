@echo off
echo ========================================
echo BUILDING JARVIS WITH CONSOLE
echo ========================================
echo.

REM Activate venv
call .venv\Scripts\activate.bat

echo Cleaning old builds...
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build

echo.
echo Building Jarvis with CONSOLE window (to see errors)...
echo This takes 5-10 minutes...
echo.

pyinstaller --clean --onedir --console --name Jarvis_AI ^
    --add-data "Frontend;Frontend" ^
    --add-data "Backend;Backend" ^
    --add-data ".env;." ^
    --hidden-import PyQt5 ^
    --hidden-import PyQt5.QtCore ^
    --hidden-import PyQt5.QtGui ^
    --hidden-import PyQt5.QtWidgets ^
    --hidden-import groq ^
    --hidden-import google.generativeai ^
    --hidden-import selenium ^
    --hidden-import pyttsx3 ^
    --hidden-import dotenv ^
    Main.py

echo.
if exist "dist\Jarvis_AI\Jarvis_AI.exe" (
    echo ✅ SUCCESS!
    echo.
    
    echo Copying .env file...
    copy .env dist\Jarvis_AI\.env
    copy .env dist\Jarvis_AI\_internal\.env 2>nul
    
    echo Creating Data folder...
    mkdir dist\Jarvis_AI\Data 2>nul
    mkdir dist\Jarvis_AI\Frontend\Files 2>nul
    
    echo Creating portable ZIP...
    powershell -Command "Compress-Archive -Path 'dist\Jarvis_AI' -DestinationPath 'Jarvis_AI_Portable.zip' -Force"
    
    echo.
    echo ========================================
    echo ✅ BUILD COMPLETE!
    echo ========================================
    echo.
    echo Executable: dist\Jarvis_AI\Jarvis_AI.exe
    echo Portable ZIP: Jarvis_AI_Portable.zip
    echo.
    echo NOTE: This version shows console window
    echo You can see errors if any occur
    echo.
    echo To test: cd dist\Jarvis_AI ^&^& Jarvis_AI.exe
    echo.
) else (
    echo ❌ Build failed!
)

pause
