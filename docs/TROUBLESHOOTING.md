# Jarvis Troubleshooting Guide

## Common Issues and Solutions

### Issue 1: Commands Not Working

**Symptoms:**
- Voice commands are recognized but nothing happens
- Jarvis says it can't find files/folders
- Operations don't execute

**Solutions:**

1. **Check if the Model is recognizing commands correctly:**
   ```bash
   python test_commands.py
   ```
   This will show you how Jarvis interprets your commands.

2. **Verify file/folder exists:**
   - Make sure the file or folder you're trying to access actually exists
   - Check common locations: Desktop, Documents, Downloads, Home folder

3. **Use specific names:**
   - Instead of: "open file report"
   - Try: "open file report.pdf" (with extension)

4. **Check permissions:**
   - Make sure you have permission to access/modify the file
   - Try running Jarvis as administrator if needed

---

### Issue 2: "Open Instagram" or Website Commands Not Working

**Symptoms:**
- Jarvis doesn't open websites like Instagram, WhatsApp, etc.

**Solutions:**

1. **Check your internet connection**

2. **Verify the command format:**
   - Correct: "Jarvis, open Instagram"
   - Correct: "Jarvis, open WhatsApp"
   - Incorrect: "Jarvis, open Instagram app"

3. **Check if browser is installed:**
   - The system needs a default web browser

4. **Test manually:**
   ```python
   from Backend.Automation import OpenApp
   OpenApp("instagram")
   ```

---

### Issue 3: Weather Commands Not Working

**Symptoms:**
- Weather information doesn't display
- Error messages about weather

**Solutions:**

1. **Check internet connection:**
   - Weather data requires internet access

2. **Use correct format:**
   - Correct: "what's the weather in New York"
   - Correct: "weather in London"
   - Correct: "tell me weather of Paris"

3. **Test manually:**
   ```python
   from Backend.Automation import GetWeather
   print(GetWeather("New York"))
   ```

---

### Issue 4: File Operations Not Working

**Symptoms:**
- Can't open, delete, or find files
- "File not found" errors

**Solutions:**

1. **Check file location:**
   - Jarvis searches in: Desktop, Documents, Downloads, Home folder
   - If your file is elsewhere, move it to one of these locations

2. **Use correct command format:**
   - For files: "open file report.pdf"
   - For folders: "open folder documents"
   - For search: "find file report.pdf"

3. **Check file name spelling:**
   - File names are case-insensitive but must be spelled correctly

4. **Test file search:**
   ```python
   from Backend.FileManager import SearchFiles
   print(SearchFiles("report"))
   ```

---

### Issue 5: Delete Confirmation Not Working

**Symptoms:**
- Files get deleted without confirmation
- Or deletion doesn't work at all

**Current Behavior:**
- The system is set up to ask for confirmation, but this needs to be integrated with the voice recognition system

**Temporary Solution:**
- Be very careful with delete commands
- Double-check file names before deleting

---

### Issue 6: Voice Recognition Issues

**Symptoms:**
- Jarvis doesn't understand your commands
- Wrong commands are executed

**Solutions:**

1. **Speak clearly and slowly**

2. **Use exact command phrases:**
   - "Jarvis, open Instagram"
   - "Jarvis, what's the weather in New York"
   - "Jarvis, find file report.pdf"

3. **Check microphone:**
   - Make sure your microphone is working
   - Check microphone permissions

4. **Reduce background noise**

---

### Issue 7: Import Errors

**Symptoms:**
- "Unable to import Backend.FileManager" error
- "Module not found" errors

**Solutions:**

1. **Check if all files exist:**
   ```bash
   dir Backend
   ```
   Should show: FileManager.py, Automation.py, Model.py, etc.

2. **Reinstall dependencies:**
   ```bash
   pip install -r Requirements.txt
   ```

3. **Check Python path:**
   - Make sure you're running from the project root directory

---

### Issue 8: Model Not Recognizing Commands

**Symptoms:**
- Commands are classified as "general" instead of specific actions
- Wrong command type detected

**Solutions:**

1. **Check API key:**
   - Make sure your Cohere API key is set in .env file
   - Verify: `CohereAPIKey=your_key_here`

2. **Test the model:**
   ```bash
   python test_commands.py
   ```

3. **Update the model:**
   - The preamble in Backend/Model.py defines how commands are recognized
   - Make sure it includes all command types

---

## Testing Individual Components

### Test File Manager:
```python
from Backend.FileManager import FileManager
fm = FileManager()

# Test search
print(fm.search_files("report"))

# Test file info
print(fm.get_file_info("report.pdf"))
```

### Test Automation:
```python
from Backend.Automation import OpenApp, GetWeather
OpenApp("instagram")
print(GetWeather("New York"))
```

### Test Model:
```python
from Backend.Model import FirstLayerDMM
print(FirstLayerDMM("open instagram"))
print(FirstLayerDMM("what's the weather in Paris"))
```

---

## Debug Mode

To see what's happening behind the scenes:

1. **Check console output:**
   - The terminal shows all command processing
   - Look for "Processing command:" messages

2. **Check decision output:**
   - Main.py prints the Decision from the model
   - Look for "Decision: [...]" in console

3. **Enable verbose logging:**
   - Add print statements in Backend/Automation.py
   - Check what commands are being received

---

## Getting Help

If none of these solutions work:

1. **Check the console for error messages**
2. **Look at the exact error text**
3. **Verify all dependencies are installed**
4. **Make sure .env file has all required API keys**

---

## Quick Command Reference

**Working Commands:**
- ✅ "open Instagram"
- ✅ "open WhatsApp"
- ✅ "what's the weather in New York"
- ✅ "open file report.pdf"
- ✅ "delete folder temp"
- ✅ "create folder projects"
- ✅ "find file document.txt"
- ✅ "show info for report.pdf"

**Command Format Tips:**
- Be specific with file names
- Include file extensions when possible
- Use clear location names for weather
- Speak naturally but clearly

---

## System Requirements

- Python 3.8+
- Windows 10/11 (primary), macOS, or Linux
- Internet connection (for weather and some features)
- Microphone for voice input
- All dependencies from Requirements.txt installed

---

## Still Having Issues?

1. Delete the `__pycache__` folders and restart
2. Restart Jarvis completely
3. Check if your .env file has all required keys
4. Verify Python version: `python --version`
5. Reinstall dependencies: `pip install -r Requirements.txt`
