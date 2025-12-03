# Create a clean distribution zip of Jarvis (without .venv and cache files)

Write-Host "Creating clean Jarvis distribution package..." -ForegroundColor Cyan

# Create temporary directory for clean files
$tempDir = "jarvis-distribution-temp"
$zipName = "jarvis-ai-assistant-complete.zip"

# Remove old temp directory if exists
if (Test-Path $tempDir) {
    Remove-Item -Recurse -Force $tempDir
}

# Create temp directory
New-Item -ItemType Directory -Path $tempDir | Out-Null

# Copy all files except excluded ones
Write-Host "Copying files..." -ForegroundColor Yellow

$excludePatterns = @(
    ".venv",
    "__pycache__",
    "*.pyc",
    "*.pyo",
    ".git",
    ".gitignore",
    "*.log",
    "jarvis-*.zip",
    $tempDir
)

# Get all items
Get-ChildItem -Path . -Recurse | ForEach-Object {
    $relativePath = $_.FullName.Substring((Get-Location).Path.Length + 1)
    
    # Check if item should be excluded
    $shouldExclude = $false
    foreach ($pattern in $excludePatterns) {
        if ($relativePath -like "*$pattern*") {
            $shouldExclude = $true
            break
        }
    }
    
    if (-not $shouldExclude) {
        $destPath = Join-Path $tempDir $relativePath
        
        if ($_.PSIsContainer) {
            # Create directory
            if (-not (Test-Path $destPath)) {
                New-Item -ItemType Directory -Path $destPath -Force | Out-Null
            }
        } else {
            # Copy file
            $destDir = Split-Path $destPath -Parent
            if (-not (Test-Path $destDir)) {
                New-Item -ItemType Directory -Path $destDir -Force | Out-Null
            }
            Copy-Item $_.FullName -Destination $destPath -Force
        }
    }
}

Write-Host "Creating zip file..." -ForegroundColor Yellow

# Remove old zip if exists
if (Test-Path $zipName) {
    Remove-Item $zipName -Force
}

# Create zip
Compress-Archive -Path "$tempDir\*" -DestinationPath $zipName -Force

# Clean up temp directory
Remove-Item -Recurse -Force $tempDir

# Show result
$zipInfo = Get-Item $zipName
$sizeMB = [math]::Round($zipInfo.Length / 1MB, 2)

Write-Host "`n✅ Success!" -ForegroundColor Green
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Green
Write-Host "Package: $zipName" -ForegroundColor Cyan
Write-Host "Size: $sizeMB MB" -ForegroundColor Cyan
Write-Host "Location: $(Get-Location)\$zipName" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Green
Write-Host "`nThis package includes:" -ForegroundColor Yellow
Write-Host "  ✓ Complete Jarvis source code" -ForegroundColor White
Write-Host "  ✓ Authentication system" -ForegroundColor White
Write-Host "  ✓ All documentation" -ForegroundColor White
Write-Host "  ✓ Requirements.txt" -ForegroundColor White
Write-Host "  ✓ Setup scripts" -ForegroundColor White
Write-Host "`nExcluded (to reduce size):" -ForegroundColor Yellow
Write-Host "  ✗ .venv folder (virtual environment)" -ForegroundColor Gray
Write-Host "  ✗ __pycache__ folders" -ForegroundColor Gray
Write-Host "  ✗ .pyc compiled files" -ForegroundColor Gray
Write-Host "`nTo use on another machine:" -ForegroundColor Cyan
Write-Host "  1. Extract the zip file" -ForegroundColor White
Write-Host "  2. Run: python -m venv .venv" -ForegroundColor White
Write-Host "  3. Activate: .venv\Scripts\activate" -ForegroundColor White
Write-Host "  4. Install: pip install -r Requirements.txt" -ForegroundColor White
Write-Host "  5. Run: python Main.py" -ForegroundColor White
