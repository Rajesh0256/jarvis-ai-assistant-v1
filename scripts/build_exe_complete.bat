@echo off
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                                                              ║
echo ║         JARVIS - COMPLETE BUILD (WITH .ENV FIX)             ║
echo ║                                                              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

REM Activate virtual environment
call .venv\Scripts\activate.bat

echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo Step 1: Cleaning old builds
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
echo Cleaned!

echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo Step 2: Building executable (5-10 minutes)
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
pyinstaller --clean Jarvis_Fixed.spec

echo.
if exist dist\Jarvis_AI\Jarvis_AI.exe (
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo ✅ BUILD SUCCESSFUL!
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo.
    
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo Step 3: Copying .env file (IMPORTANT!)
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    copy .env dist\Jarvis_AI\.env
    if exist dist\Jarvis_AI\.env (
        echo ✅ .env file copied successfully!
    ) else (
        echo ❌ Failed to copy .env file!
    )
    
    echo.
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo Step 4: Creating portable ZIP
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    if exist Jarvis_AI_Portable.zip del Jarvis_AI_Portable.zip
    powershell -Command "Compress-Archive -Path 'dist\Jarvis_AI\*' -DestinationPath 'Jarvis_AI_Portable.zip' -Force"
    
    if exist Jarvis_AI_Portable.zip (
        echo ✅ Portable ZIP created!
        for %%A in (Jarvis_AI_Portable.zip) do echo    Size: %%~zA bytes
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
    echo.
    Jarvis_AI.exe
    
    cd ..\..
    
    echo.
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo 🎉 COMPLETE!
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo.
    echo ✅ Executable: dist\Jarvis_AI\Jarvis_AI.exe
    echo ✅ Portable:   Jarvis_AI_Portable.zip
    echo ✅ .env file:  Included!
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
)

echo.
pause
