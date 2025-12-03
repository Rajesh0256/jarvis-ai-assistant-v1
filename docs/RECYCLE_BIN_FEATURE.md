# Recycle Bin Management Feature 🗑️

## Overview
Jarvis can now manage your Windows Recycle Bin with voice commands! You can open it, check its contents, and empty it completely.

## Available Commands

### 1. Open Recycle Bin
**Voice Commands:**
- "Jarvis, open recycle bin"
- "Jarvis, show recycle bin"
- "Jarvis, open trash"

**What it does:** Opens the Recycle Bin window so you can see all deleted files.

**Example:**
```
You: "Jarvis, open recycle bin"
Jarvis: "Opening Recycle Bin for you"
→ Recycle Bin window opens
```

---

### 2. Empty Recycle Bin
**Voice Commands:**
- "Jarvis, empty recycle bin"
- "Jarvis, clear recycle bin"
- "Jarvis, delete all files from recycle bin"
- "Jarvis, empty trash"

**What it does:** Permanently deletes ALL files from the Recycle Bin. This action cannot be undone!

**Example:**
```
You: "Jarvis, empty recycle bin"
Jarvis: "Successfully emptied the Recycle Bin. All files have been permanently deleted."
→ All files in Recycle Bin are permanently deleted
```

⚠️ **WARNING:** This permanently deletes all files! They cannot be recovered!

---

### 3. Get Recycle Bin Info
**Voice Commands:**
- "Jarvis, recycle bin info"
- "Jarvis, how many files in recycle bin"
- "Jarvis, what's in the trash"

**What it does:** Tells you how many items are in the Recycle Bin and their total size.

**Example:**
```
You: "Jarvis, recycle bin info"
Jarvis: "The Recycle Bin contains 15 items, total size: 245.67 MB"
```

---

## How It Works

### Technical Details:

1. **Open Recycle Bin:**
   - Uses Windows `shell:RecycleBinFolder` command
   - Opens in File Explorer
   - Works on Windows 10/11

2. **Empty Recycle Bin:**
   - Uses `winshell` library (preferred method)
   - Falls back to PowerShell if winshell not available
   - Empties without confirmation for voice convenience
   - Permanently deletes all files

3. **Get Info:**
   - Uses `winshell` to enumerate items
   - Calculates total size
   - Returns count and size in human-readable format

---

## Use Cases

### Scenario 1: Quick Cleanup
```
"Jarvis, open recycle bin"
→ Check what's in there
"Jarvis, empty recycle bin"
→ Clean up space
```

### Scenario 2: Check Before Emptying
```
"Jarvis, recycle bin info"
→ "The Recycle Bin contains 50 items, total size: 1.2 GB"
"Jarvis, empty recycle bin"
→ Free up 1.2 GB of space
```

### Scenario 3: Regular Maintenance
```
"Jarvis, how many files in recycle bin"
→ Check if cleanup is needed
"Jarvis, empty recycle bin"
→ Perform cleanup
```

---

## Important Safety Notes

### ⚠️ CRITICAL WARNINGS:

1. **Permanent Deletion:**
   - Emptying the Recycle Bin is PERMANENT
   - Files cannot be recovered after emptying
   - Make sure you don't need any files before emptying

2. **No Confirmation:**
   - For voice convenience, there's no confirmation prompt
   - Be absolutely sure before saying "empty recycle bin"
   - Double-check with "recycle bin info" first

3. **All Files Deleted:**
   - The command empties the ENTIRE Recycle Bin
   - You cannot selectively delete individual files via voice
   - To delete specific files, open Recycle Bin manually

---

## Platform Support

### Windows (Fully Supported):
- ✅ Open Recycle Bin
- ✅ Empty Recycle Bin
- ✅ Get Recycle Bin Info

### macOS (Basic Support):
- ✅ Open Trash
- ✅ Empty Trash
- ❌ Get Trash Info (not available)

### Linux (Basic Support):
- ✅ Open Trash
- ✅ Empty Trash
- ❌ Get Trash Info (not available)

---

## Troubleshooting

### Issue: "winshell not found"
**Solution:**
```bash
pip install winshell
```

### Issue: Empty command doesn't work
**Solution:**
- Make sure you're on Windows
- Try the PowerShell fallback (automatic)
- Check if you have admin permissions

### Issue: Can't open Recycle Bin
**Solution:**
- Make sure File Explorer is working
- Try opening manually first
- Restart Jarvis

---

## Command Flow

### Example: Empty Recycle Bin

1. **Voice Input:**
   ```
   "Jarvis, empty recycle bin"
   ```

2. **Model Recognition:**
   ```
   Decision: ['empty recycle bin']
   ```

3. **Automation:**
   ```
   Processing command: empty recycle bin
   Calling: EmptyRecycleBin()
   ```

4. **Execution:**
   ```
   - Checks if Windows
   - Uses winshell or PowerShell
   - Empties Recycle Bin
   - Returns success message
   ```

5. **Response:**
   ```
   Jarvis: "Successfully emptied the Recycle Bin. All files have been permanently deleted."
   ```

---

## Best Practices

### ✅ DO:
- Check Recycle Bin info before emptying
- Open Recycle Bin to verify contents
- Use regularly for disk space management
- Be specific with your commands

### ❌ DON'T:
- Empty without checking first
- Use if you're unsure about deleted files
- Rely on it for important file recovery
- Use if you might need deleted files later

---

## Testing

### Test Open:
```python
from Backend.FileManager import OpenRecycleBin
print(OpenRecycleBin())
```

### Test Info:
```python
from Backend.FileManager import GetRecycleBinInfo
print(GetRecycleBinInfo())
```

### Test Empty (BE CAREFUL!):
```python
from Backend.FileManager import EmptyRecycleBin
# Only run if you're sure!
# print(EmptyRecycleBin())
```

---

## Integration with Other Features

### Combined Commands:
```
"Jarvis, delete folder old_projects and empty recycle bin"
→ Deletes folder, then empties Recycle Bin

"Jarvis, open recycle bin and show me the info"
→ Opens Recycle Bin and tells you the info
```

---

## FAQ

**Q: Can I recover files after emptying?**
A: No, emptying the Recycle Bin permanently deletes files.

**Q: Can I delete specific files from Recycle Bin?**
A: Not via voice. Use "open recycle bin" and delete manually.

**Q: How often should I empty the Recycle Bin?**
A: Depends on your usage. Check with "recycle bin info" regularly.

**Q: Does it work on Mac/Linux?**
A: Basic functionality yes, but info feature is Windows-only.

**Q: Is it safe to use?**
A: Yes, but be careful! Deletion is permanent.

---

## Dependencies

- **winshell** (Windows only): For Recycle Bin operations
- **PowerShell** (fallback): Built into Windows
- **os.startfile**: For opening Recycle Bin

Install dependencies:
```bash
pip install winshell
```

---

## Summary

The Recycle Bin feature gives you voice-controlled access to Windows Recycle Bin management. Use it responsibly, always check before emptying, and enjoy the convenience of hands-free disk cleanup!

🎉 **Feature Status: FULLY WORKING**

---

## Quick Reference

| Command | Action | Reversible |
|---------|--------|------------|
| "open recycle bin" | Opens Recycle Bin window | N/A |
| "empty recycle bin" | Permanently deletes all files | ❌ NO |
| "recycle bin info" | Shows count and size | N/A |

Remember: **Always check before you empty!** 🗑️
