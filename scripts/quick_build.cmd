@echo off
echo ============================================================
echo JARVIS - QUICK EXE BUILDER
echo ============================================================
echo.
echo Building Jarvis.exe...
echo This will take 5-10 minutes, please wait...
echo.

cd /d "%~dp0"
python -m PyInstaller --clean Jarvis.spec

echo.
if exist "dist\Jarvis\Jarvis.exe" (
    echo ============================================================
    echo SUCCESS! Jarvis.exe created at: dist\Jarvis\Jarvis.exe
    echo ============================================================
    echo.
    echo Opening folder...
    explorer dist\Jarvis
) else (
    echo ============================================================
    echo BUILD FAILED! Check errors above.
    echo ============================================================
)

echo.
pause
