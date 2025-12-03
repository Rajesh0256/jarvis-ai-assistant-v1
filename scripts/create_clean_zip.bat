@echo off
echo ========================================
echo Creating Clean Jarvis Distribution
echo ========================================
echo.

echo Removing old zip files...
if exist jarvis-ai-assistant-complete.zip del jarvis-ai-assistant-complete.zip
if exist jarvis-distribution-temp rmdir /s /q jarvis-distribution-temp

echo Creating temporary directory...
mkdir jarvis-distribution-temp

echo Copying files (excluding .venv and cache)...
xcopy /E /I /Y /EXCLUDE:zip_exclude.txt . jarvis-distribution-temp

echo Creating zip file...
powershell -Command "Compress-Archive -Path 'jarvis-distribution-temp\*' -DestinationPath 'jarvis-ai-assistant-complete.zip' -Force"

echo Cleaning up...
rmdir /s /q jarvis-distribution-temp

echo.
echo ========================================
echo ✅ Success!
echo ========================================
echo Package: jarvis-ai-assistant-complete.zip
echo.
dir jarvis-ai-assistant-complete.zip
echo.
echo This package is ready to share!
echo ========================================
pause
