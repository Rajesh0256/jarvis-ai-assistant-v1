@echo off
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                                                              ║
echo ║         JARVIS - QUICK FIX FOR .ENV ERROR                   ║
echo ║                                                              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo Step 1: Testing Python script first
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.
echo If this works, we'll rebuild the exe...
echo.
pause

python Main.py

echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo Did the Python script work? (Y/N)
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
set /p answer=Enter Y to rebuild exe, N to exit: 

if /i "%answer%"=="Y" (
    echo.
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo Step 2: Rebuilding executable
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo.
    
    REM Clean old builds
    if exist build rmdir /s /q build
    if exist dist rmdir /s /q dist
    
    REM Rebuild
    python -m PyInstaller --clean Jarvis_Fixed.spec
    
    echo.
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo Step 3: Testing executable
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo.
    
    if exist dist\Jarvis_AI\Jarvis_AI.exe (
        echo ✅ Executable created!
        echo.
        echo Testing now...
        echo.
        cd dist\Jarvis_AI
        Jarvis_AI.exe
        cd ..\..
    ) else (
        echo ❌ Build failed!
    )
)

echo.
pause
