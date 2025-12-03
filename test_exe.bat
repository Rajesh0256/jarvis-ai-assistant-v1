@echo off
echo ========================================
echo TESTING JARVIS EXECUTABLE
echo ========================================
echo.

echo Checking if EXE exists...
if not exist "dist\Jarvis_AI\Jarvis_AI.exe" (
    echo ❌ EXE not found! Build it first.
    pause
    exit
)

echo ✅ EXE found!
echo.

echo Checking .env file...
if not exist "dist\Jarvis_AI\.env" (
    echo ⚠️ .env missing! Copying...
    copy .env dist\Jarvis_AI\.env
)

echo Checking Data folder...
if not exist "dist\Jarvis_AI\Data" (
    echo ⚠️ Data folder missing! Creating...
    mkdir dist\Jarvis_AI\Data
)

echo Checking Frontend\Files folder...
if not exist "dist\Jarvis_AI\Frontend\Files" (
    echo ⚠️ Frontend\Files missing! Creating...
    mkdir dist\Jarvis_AI\Frontend\Files
)

echo.
echo ========================================
echo RUNNING JARVIS...
echo ========================================
echo.
echo If it closes immediately, you'll see the error here.
echo.

cd dist\Jarvis_AI
Jarvis_AI.exe

echo.
echo ========================================
echo Jarvis closed.
echo ========================================
pause
