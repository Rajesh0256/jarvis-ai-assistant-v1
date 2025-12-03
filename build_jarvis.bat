@echo off
echo ========================================
echo BUILDING JARVIS EXECUTABLE
echo ========================================
echo.

REM Activate virtual environment
call .venv\Scripts\activate.bat

echo Step 1: Cleaning old builds...
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build
echo Cleaned!
echo.

echo Step 2: Building with PyInstaller...
echo This will take 5-10 minutes...
echo.

REM Build using the spec file from build_tools
pyinstaller --clean build_tools\Jarvis_Complete.spec

echo.
echo Step 3: Checking if build succeeded...
if exist "dist\Main\Main.exe" (
    echo ✅ Build successful!
    echo.
    
    echo Step 4: Copying .env file...
    copy .env dist\Main\.env
    
    echo Step 5: Creating Data folder...
    mkdir dist\Main\Data 2>nul
    
    echo Step 6: Creating portable ZIP...
    powershell -Command "Compress-Archive -Path 'dist\Main\*' -DestinationPath 'Jarvis_AI_Portable.zip' -Force"
    
    echo.
    echo ========================================
    echo ✅ BUILD COMPLETE!
    echo ========================================
    echo.
    echo Executable: dist\Main\Main.exe
    echo Portable ZIP: Jarvis_AI_Portable.zip
    echo.
    echo To test: cd dist\Main ^&^& Main.exe
    echo.
) else (
    echo ❌ Build failed! Check errors above.
    echo.
    echo Common issues:
    echo - Missing dependencies: pip install -r Requirements.txt
    echo - PyInstaller not installed: pip install pyinstaller
    echo.
)

pause
