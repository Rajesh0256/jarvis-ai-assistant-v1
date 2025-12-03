@echo off
title Jarvis EXE Builder
color 0A
echo.
echo ============================================================
echo          JARVIS AI ASSISTANT - EXE BUILDER
echo ============================================================
echo.
echo This will create a standalone executable for Jarvis.
echo The process may take 5-10 minutes.
echo.
echo What will be created:
echo  - Jarvis.exe (standalone executable)
echo  - All required files bundled together
echo  - No Python installation needed to run!
echo.
echo Requirements:
echo  - 2GB free disk space
echo  - PyInstaller installed (checking...)
echo.

REM Check if PyInstaller is installed
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo [ERROR] PyInstaller is not installed!
    echo.
    echo Installing PyInstaller...
    pip install pyinstaller
    if errorlevel 1 (
        echo [ERROR] Failed to install PyInstaller!
        pause
        exit /b 1
    )
)

echo [OK] PyInstaller is installed
echo.
echo Press any key to start building...
pause > nul

echo.
echo [1/4] Cleaning previous builds...
if exist build (
    echo Removing old build folder...
    rmdir /s /q build
)
if exist dist (
    echo Removing old dist folder...
    rmdir /s /q dist
)
echo [OK] Cleanup complete

echo.
echo [2/4] Checking required files...
if not exist "Main.py" (
    echo [ERROR] Main.py not found!
    pause
    exit /b 1
)
if not exist "Jarvis.spec" (
    echo [ERROR] Jarvis.spec not found!
    pause
    exit /b 1
)
echo [OK] All required files present

echo.
echo [3/4] Building executable with PyInstaller...
echo This may take 5-10 minutes, please be patient...
echo.
python -m PyInstaller --clean --noconfirm Jarvis.spec

echo.
echo [4/4] Checking build status...
if exist "dist\Jarvis\Jarvis.exe" (
    echo.
    echo ============================================================
    echo              BUILD SUCCESSFUL!
    echo ============================================================
    echo.
    echo Your executable has been created!
    echo.
    echo Location: dist\Jarvis\Jarvis.exe
    echo.
    echo File size: 
    for %%A in ("dist\Jarvis\Jarvis.exe") do echo   %%~zA bytes
    echo.
    echo To run Jarvis:
    echo   1. Go to: dist\Jarvis\
    echo   2. Double-click: Jarvis.exe
    echo.
    echo To distribute:
    echo   - Zip the entire "dist\Jarvis" folder
    echo   - Share the zip file
    echo   - Recipients just extract and run!
    echo.
    echo IMPORTANT: Keep all files in the Jarvis folder together!
    echo.
    echo ============================================================
    echo.
    echo Press any key to open the dist folder...
    pause > nul
    explorer dist\Jarvis
) else (
    echo.
    echo ============================================================
    echo              BUILD FAILED!
    echo ============================================================
    echo.
    echo Please check the error messages above.
    echo.
    echo Common issues:
    echo   - Missing dependencies (run: pip install -r Requirements.txt)
    echo   - Antivirus blocking PyInstaller (disable temporarily)
    echo   - Insufficient disk space (need 2GB free)
    echo   - Python processes still running (close all)
    echo.
    echo Solutions:
    echo   1. Close all Python/Jarvis processes
    echo   2. Disable antivirus temporarily
    echo   3. Run as administrator
    echo   4. Check disk space
    echo.
    echo Press any key to exit...
    pause > nul
    exit /b 1
)
