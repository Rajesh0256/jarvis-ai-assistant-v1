@echo off
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                                                              ║
echo ║         JARVIS AI - Windows Executable Builder              ║
echo ║                                                              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

REM Check if virtual environment is activated
if not defined VIRTUAL_ENV (
    echo Activating virtual environment...
    call .venv\Scripts\activate.bat
)

echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo Step 1: Installing PyInstaller
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
pip install pyinstaller
echo.

echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo Step 2: Cleaning old build files
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
echo Old build files cleaned!
echo.

echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo Step 3: Building Jarvis executable
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo This may take 5-10 minutes...
echo.
pyinstaller --clean Jarvis_Complete.spec
echo.

if exist dist\Jarvis_AI (
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo ✅ SUCCESS! Jarvis executable created!
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo.
    echo 📁 Location: dist\Jarvis_AI\
    echo 🚀 Executable: dist\Jarvis_AI\Jarvis_AI.exe
    echo.
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo Step 4: Creating distribution package
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    REM Create README for distribution
    echo Creating README...
    (
        echo ╔══════════════════════════════════════════════════════════════╗
        echo ║                                                              ║
        echo ║              JARVIS AI ASSISTANT - WINDOWS                   ║
        echo ║                                                              ║
        echo ╚══════════════════════════════════════════════════════════════╝
        echo.
        echo 🚀 HOW TO RUN:
        echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        echo.
        echo 1. Double-click: Jarvis_AI.exe
        echo 2. Login page will appear
        echo 3. Create account or login
        echo 4. Enjoy Jarvis!
        echo.
        echo 📋 FEATURES:
        echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        echo.
        echo ✓ Secure authentication system
        echo ✓ Voice recognition
        echo ✓ AI-powered responses
        echo ✓ File management
        echo ✓ System automation
        echo ✓ Web search
        echo ✓ And much more!
        echo.
        echo 📁 FOLDER STRUCTURE:
        echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        echo.
        echo Jarvis_AI/
        echo ├── Jarvis_AI.exe          ^(Main executable^)
        echo ├── Data/                  ^(User data, chat logs^)
        echo ├── Frontend/              ^(GUI files, graphics^)
        echo ├── Backend/               ^(AI logic, automation^)
        echo └── Other dependencies...
        echo.
        echo ⚙️ CONFIGURATION:
        echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        echo.
        echo Edit .env file to customize:
        echo - Username
        echo - Assistant name
        echo - API keys
        echo.
        echo 🔐 SECURITY:
        echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        echo.
        echo - Passwords are encrypted with SHA-256
        echo - User data stored locally in Data/users.json
        echo - No data sent to external servers
        echo.
        echo 💡 TIPS:
        echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        echo.
        echo - Press Enter to login quickly
        echo - Click microphone to activate voice commands
        echo - Check Data/ChatLog.json for conversation history
        echo.
        echo 🆘 TROUBLESHOOTING:
        echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        echo.
        echo Problem: Antivirus blocks the exe
        echo Solution: Add exception for Jarvis_AI.exe
        echo.
        echo Problem: Missing DLL errors
        echo Solution: Install Visual C++ Redistributable
        echo.
        echo Problem: Forgot password
        echo Solution: Delete Data/users.json and create new account
        echo.
        echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        echo Enjoy your AI assistant! 🤖
        echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ) > dist\Jarvis_AI\README.txt
    
    echo ✅ README.txt created
    echo.
    
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo Step 5: Creating portable ZIP package
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    if exist Jarvis_AI_Portable.zip del Jarvis_AI_Portable.zip
    powershell -Command "Compress-Archive -Path 'dist\Jarvis_AI\*' -DestinationPath 'Jarvis_AI_Portable.zip' -Force"
    
    if exist Jarvis_AI_Portable.zip (
        echo ✅ Portable package created: Jarvis_AI_Portable.zip
        echo.
        
        REM Get file size
        for %%A in (Jarvis_AI_Portable.zip) do (
            set size=%%~zA
            set /a sizeMB=!size! / 1048576
        )
        
        echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        echo 🎉 BUILD COMPLETE!
        echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        echo.
        echo 📦 Distribution Package: Jarvis_AI_Portable.zip
        echo 📁 Executable Folder: dist\Jarvis_AI\
        echo 🚀 Run: dist\Jarvis_AI\Jarvis_AI.exe
        echo.
        echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        echo TO USE ON ANOTHER PC:
        echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        echo.
        echo 1. Copy Jarvis_AI_Portable.zip to the other PC
        echo 2. Extract the ZIP file
        echo 3. Double-click Jarvis_AI.exe
        echo 4. No Python installation needed!
        echo.
        echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        REM Open the dist folder
        explorer dist\Jarvis_AI
    )
) else (
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo ❌ BUILD FAILED!
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo.
    echo Check the error messages above.
    echo Common issues:
    echo - Missing dependencies
    echo - Incorrect file paths
    echo - Antivirus interference
    echo.
)

echo.
pause
