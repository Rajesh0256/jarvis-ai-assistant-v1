# Start Jarvis with Floating Input Window
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting Jarvis with Floating Input" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Activate virtual environment
& .\.venv\Scripts\Activate.ps1

# Start floating input in new window
Write-Host "Starting floating input window..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "& .\.venv\Scripts\Activate.ps1; python start_floating_input.py"

# Wait a moment
Start-Sleep -Seconds 2

# Start Jarvis main
Write-Host "Starting Jarvis..." -ForegroundColor Yellow
python Main.py
