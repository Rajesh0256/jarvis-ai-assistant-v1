@echo off
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                                                              ║
echo ║         JARVIS - BUILD WINDOWS EXECUTABLE (FINAL)           ║
echo ║                                                              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo Step 1: Verifying PyInstaller
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
pip show pyinstaller
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
)

echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo Step 2: Cleaning old builds
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
echo Cleaned!

echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo Step 3: Building executable (this takes 5-10 minutes)
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.
pyinstaller --clean Jarvis_Fixed.spec

echo.
if exist dist\Jarvis_AI\Jarvis_AI.exe (
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo ✅ BUILD SUCCESSFUL!
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo.
    echo 📁 Location: dist\Jarvis_AI\
    echo 🚀 Executable: dist\Jarvis_AI\Jarvis_AI.exe
    echo.
    
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo Step 4: Creating portable ZIP
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    if exist Jarvis_AI_Portable.zip del Jarvis_AI_Portable.zip
    powershell -Command "Compress-Archive -Path 'dist\Jarvis_AI\*' -DestinationPath 'Jarvis_AI_Portable.zip' -Force"
    
    if exist Jarvis_AI_Portable.zip (
        echo ✅ Portable ZIP created: Jarvis_AI_Portable.zip
    )
    
    echo.
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo Step 5: Testing executable
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo.
    echo Press any key to test the executable...
    pause > nul
    
    cd dist\Jarvis_AI
    echo.
    echo Running Jarvis_AI.exe...
    echo (Console will stay open to show any errors)
    echo.
    Jarvis_AI.exe
    
    cd ..\..
    
    echo.
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo 🎉 ALL DONE!
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo.
    echo Your Jarvis Windows application is ready!
    echo.
    echo 📦 Executable: dist\Jarvis_AI\Jarvis_AI.exe
    echo 📦 Portable:   Jarvis_AI_Portable.zip
    echo.
    echo To use on another PC:
    echo 1. Copy Jarvis_AI_Portable.zip
    echo 2. Extract anywhere
    echo 3. Double-click Jarvis_AI.exe
    echo.
    
    explorer dist\Jarvis_AI
) else (
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo ❌ BUILD FAILED!
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo.
    echo Check the error messages above.
    echo.
)

echo.
pause
