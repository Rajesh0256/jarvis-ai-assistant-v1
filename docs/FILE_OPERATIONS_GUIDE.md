# Jarvis File & Folder Operations Guide

## Overview
Jarvis now has comprehensive file and folder management capabilities. You can use voice commands to manage your files and folders without touching your keyboard!

## Available Commands

### 1. OPEN FILE OR FOLDER
**Voice Commands:**
- "Jarvis, open file report.pdf"
- "Jarvis, open folder documents"
- "Jarvis, open downloads folder"

**What it does:** Opens the specified file or folder using your system's default application.

---

### 2. DELETE FILE OR FOLDER
**Voice Commands:**
- "Jarvis, delete file old_report.pdf"
- "Jarvis, delete folder temp"

**What it does:** Deletes the specified file or folder. For safety, Jarvis will ask for confirmation before deleting.

**Important:** For voice convenience, delete operations execute immediately. Please be careful and specific with file/folder names to avoid accidental deletion.

---

### 3. CREATE FOLDER
**Voice Commands:**
- "Jarvis, create a new folder named projects"
- "Jarvis, create folder work"
- "Jarvis, make a folder called documents"

**What it does:** Creates a new folder on your Desktop (default location).

---

### 4. SEARCH FOR FILES
**Voice Commands:**
- "Jarvis, find file report.pdf"
- "Jarvis, search for document.txt"
- "Jarvis, find presentation"

**What it does:** Searches for files/folders in common locations:
- Desktop
- Documents
- Downloads
- Home folder

**Result:** Lists all matching files with their full paths.

---

### 5. GET FILE INFORMATION
**Voice Commands:**
- "Jarvis, show info for report.pdf"
- "Jarvis, what's the size of document.txt"
- "Jarvis, file info presentation.pptx"

**What it does:** Displays detailed information about a file:
- File type
- File size (in bytes, KB, MB, or GB)
- Creation date
- Last modified date
- Full file path

---

### 6. RENAME FILE OR FOLDER
**Voice Commands:**
- "Jarvis, rename file old.txt to new.txt"
- "Jarvis, rename folder oldname to newname"

**What it does:** Renames the specified file or folder.

---

### 7. WEATHER INFORMATION
**Voice Commands:**
- "Jarvis, what's the weather in New York?"
- "Jarvis, tell me weather of London"
- "Jarvis, weather in Mumbai"

**What it does:** Fetches real-time weather information including:
- Current conditions
- Temperature
- Humidity
- Wind speed

---

### 8. OPEN WEBSITES
**Voice Commands:**
- "Jarvis, open Instagram"
- "Jarvis, open WhatsApp"
- "Jarvis, open YouTube"

**Supported Websites:**
- Instagram, WhatsApp, Facebook, Twitter/X
- YouTube, Gmail, LinkedIn, Reddit, GitHub
- Netflix, Amazon, Spotify, Discord, Telegram
- Pinterest, TikTok, Snapchat, Twitch
- Zoom, Slack, Teams, Outlook
- Google, Drive, Maps

---

## How It Works

1. **Voice Recognition:** Jarvis listens to your voice command
2. **Command Processing:** The AI model identifies what type of operation you want
3. **Execution:** Jarvis performs the requested operation
4. **Feedback:** Jarvis speaks back to confirm the action

## Search Locations

Jarvis searches for files in these common locations:
- `C:\Users\[YourName]\Desktop`
- `C:\Users\[YourName]\Documents`
- `C:\Users\[YourName]\Downloads`
- `C:\Users\[YourName]` (Home folder)

## Safety Features

- **Delete Confirmation:** Always asks before deleting files/folders
- **Error Handling:** Gracefully handles missing files or permission errors
- **Clear Feedback:** Provides clear spoken responses about what happened

## Examples

### Example 1: Opening a File
**You:** "Jarvis, open file report.pdf"
**Jarvis:** "Opening report.pdf for you"

### Example 2: Creating a Folder
**You:** "Jarvis, create a new folder named work projects"
**Jarvis:** "Created new folder work projects at C:\Users\YourName\Desktop"

### Example 3: Getting Weather
**You:** "Jarvis, what's the weather in Paris?"
**Jarvis:** "Weather in Paris: Clear 15°C 65% 10km/h"

### Example 4: Searching for Files
**You:** "Jarvis, find file presentation"
**Jarvis:** "I found 3 items matching presentation:
1. C:\Users\YourName\Documents\presentation.pptx
2. C:\Users\YourName\Desktop\presentation_final.pptx
3. C:\Users\YourName\Downloads\presentation_backup.pptx"

## Tips

1. **Be Specific:** Use clear file names for better results
2. **File Extensions:** You can include or omit file extensions (e.g., "report.pdf" or just "report")
3. **Case Insensitive:** Jarvis searches are case-insensitive
4. **Multiple Results:** If multiple files match, Jarvis will list them all

## Troubleshooting

**Problem:** "I couldn't find [filename]"
**Solution:** 
- Make sure the file exists in common locations
- Try using a more specific file name
- Check if the file is in a different location

**Problem:** "Permission denied"
**Solution:** 
- Make sure you have permission to access/modify the file
- Try running Jarvis as administrator (if needed)

**Problem:** File operation doesn't work
**Solution:**
- Check that the file/folder name is correct
- Ensure the file isn't open in another program
- Verify you have the necessary permissions

## Technical Details

- **Platform:** Windows (with cross-platform support for macOS and Linux)
- **Search Depth:** Up to 3 levels deep in each search location
- **File Size Display:** Automatically converts to appropriate units (bytes, KB, MB, GB)
- **Date Format:** YYYY-MM-DD HH:MM:SS

---

Enjoy your enhanced Jarvis experience! 🚀
