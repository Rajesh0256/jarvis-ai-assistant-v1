# How to Build Jarvis.exe - Simple Instructions

## The Issue

PyInstaller is installed but not accessible in the current virtual environment path. Here's how to fix it and build your EXE.

---

## Solution: Build Outside Virtual Environment

### Step 1: Open Fresh Command Prompt

1. Press `Win + R`
2. Type `cmd`
3. Press Enter

### Step 2: Navigate to Project

```cmd
cd "C:\Users\RAJESH\Documents\rajesh\mark6\jarvis-ai-assistant-main"
```

### Step 3: Install PyInstaller Globally (if needed)

```cmd
pip install pyinstaller
```

### Step 4: Build the EXE

```cmd
pyinstaller --clean Jarvis.spec
```

**Wait 5-10 minutes** for the build to complete.

### Step 5: Find Your EXE

```
dist\Jarvis\Jarvis.exe
```

---

## Alternative: Use Python Directly

If pyinstaller command doesn't work, try:

```cmd
python -m PyInstaller --clean Jarvis.spec
```

---

## Quick Build Script

Save this as `quick_build.cmd`:

```cmd
@echo off
cd /d "%~dp0"
python -m PyInstaller --clean Jarvis.spec
pause
```

Then just double-click `quick_build.cmd`!

---

## What to Expect

### During Build:
```
Analyzing Main.py...
Building EXE...
Copying files...
Done!
```

### After Build:
```
dist/
└── Jarvis/
    ├── Jarvis.exe  ← Your executable!
    └── [many files]
```

---

## If Build Fails

### Error: "pyinstaller not found"

**Solution:**
```cmd
pip install --user pyinstaller
```

Then try again.

### Error: "Module not found"

**Solution:**
```cmd
pip install -r Requirements.txt
```

Then rebuild.

### Error: "Permission denied"

**Solution:**
- Run Command Prompt as Administrator
- Disable antivirus temporarily

---

## Testing the EXE

```cmd
cd dist\Jarvis
Jarvis.exe
```

---

## Summary

**Easiest way:**
1. Open Command Prompt (not PowerShell)
2. Navigate to project folder
3. Run: `python -m PyInstaller --clean Jarvis.spec`
4. Wait 5-10 minutes
5. Find EXE in: `dist\Jarvis\Jarvis.exe`

**That's it!** 🚀
