@echo off
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                                                              ║
echo ║         JARVIS - FINAL BUILD (ALL FIXES INCLUDED)           ║
echo ║                                                              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

call .venv\Scripts\activate.bat

echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo Cleaning and rebuilding...
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

pyinstaller --clean Jarvis_Fixed.spec

if exist dist\Jarvis_AI\Jarvis_AI.exe (
    echo.
    echo ✅ Build successful!
    echo.
    
    REM Copy .env
    copy .env dist\Jarvis_AI\.env > nul
    echo ✅ .env copied
    
    REM Create Data folder
    if not exist dist\Jarvis_AI\Data mkdir dist\Jarvis_AI\Data
    echo ✅ Data folder created
    
    REM Create empty ChatLog.json
    echo [] > dist\Jarvis_AI\Data\ChatLog.json
    echo ✅ ChatLog.json created
    
    REM Create portable ZIP
    if exist Jarvis_AI_Portable.zip del Jarvis_AI_Portable.zip
    powershell -Command "Compress-Archive -Path 'dist\Jarvis_AI\*' -DestinationPath 'Jarvis_AI_Portable.zip' -Force"
    echo ✅ Portable ZIP created
    
    echo.
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo 🎉 BUILD COMPLETE!
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo.
    echo ✅ Executable: dist\Jarvis_AI\Jarvis_AI.exe
    echo ✅ Portable:   Jarvis_AI_Portable.zip
    echo ✅ Size:       ~153 MB
    echo.
    echo Press any key to test...
    pause > nul
    
    cd dist\Jarvis_AI
    echo.
    echo Testing Jarvis_AI.exe...
    echo.
    Jarvis_AI.exe
    
    cd ..\..
    
    echo.
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo If it worked, you're done!
    echo Share: Jarvis_AI_Portable.zip
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    explorer dist\Jarvis_AI
) else (
    echo ❌ Build failed!
)

pause
