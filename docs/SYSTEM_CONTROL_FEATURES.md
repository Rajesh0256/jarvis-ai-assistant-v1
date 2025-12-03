# System Control Features 🖥️

## Overview
Jarvis can now control your PC with voice commands! Close windows, shutdown, restart, sleep, lock, and more!

## Available Commands

### 1. Close Current Window
**Voice Commands:**
- "Jarvis, close current window"
- "Jarvis, close this window"
- "Jarvis, close window"

**What it does:** Closes the currently active window (Alt+F4)

**Example:**
```
You: "Jarvis, close current window"
Jarvis: "Closing current window sir"
→ Current window closes
```

---

### 2. Shutdown PC
**Voice Commands:**
- "Jarvis, shutdown PC"
- "Jarvis, shutdown computer"
- "Jarvis, turn off PC"

**What it does:** Shuts down your computer in 5 seconds

**Example:**
```
You: "Jarvis, shutdown PC"
Jarvis: "Shutting down PC in 5 seconds sir. Say cancel shutdown to stop."
→ PC shuts down in 5 seconds
```

⚠️ **Warning:** This will actually shutdown your PC! Make sure to save your work first.

---

### 3. Restart PC
**Voice Commands:**
- "Jarvis, restart PC"
- "Jarvis, restart computer"
- "Jarvis, reboot PC"

**What it does:** Restarts your computer in 5 seconds

**Example:**
```
You: "Jarvis, restart PC"
Jarvis: "Restarting PC in 5 seconds sir. Say cancel restart to stop."
→ PC restarts in 5 seconds
```

---

### 4. Cancel Shutdown/Restart
**Voice Commands:**
- "Jarvis, cancel shutdown"
- "Jarvis, cancel restart"
- "Jarvis, stop shutdown"

**What it does:** Cancels a scheduled shutdown or restart

**Example:**
```
You: "Jarvis, shutdown PC"
Jarvis: "Shutting down PC in 5 seconds sir..."
You: "Jarvis, cancel shutdown"
Jarvis: "Shutdown cancelled sir"
→ Shutdown is cancelled
```

---

### 5. Sleep PC
**Voice Commands:**
- "Jarvis, sleep PC"
- "Jarvis, put PC to sleep"
- "Jarvis, sleep computer"

**What it does:** Puts your PC into sleep mode

**Example:**
```
You: "Jarvis, sleep PC"
Jarvis: "Putting PC to sleep sir"
→ PC goes to sleep
```

---

### 6. Lock PC
**Voice Commands:**
- "Jarvis, lock PC"
- "Jarvis, lock computer"
- "Jarvis, lock my PC"

**What it does:** Locks your PC (requires password to unlock)

**Example:**
```
You: "Jarvis, lock PC"
Jarvis: "Locking PC sir"
→ PC locks, login screen appears
```

---

### 7. Volume Controls (Existing)
**Voice Commands:**
- "Jarvis, mute"
- "Jarvis, unmute"
- "Jarvis, volume up"
- "Jarvis, volume down"

**What it does:** Controls system volume

---

## How It Works

### Technical Implementation:

1. **Close Window:**
   - Sends Alt+F4 keyboard shortcut
   - Closes the currently focused window

2. **Shutdown:**
   - Windows: `shutdown /s /t 5`
   - Gives 5 seconds to cancel
   - Can be cancelled with "cancel shutdown"

3. **Restart:**
   - Windows: `shutdown /r /t 5`
   - Gives 5 seconds to cancel
   - Can be cancelled with "cancel restart"

4. **Sleep:**
   - Windows: Uses `rundll32.exe powrprof.dll,SetSuspendState`
   - Immediately puts PC to sleep

5. **Lock:**
   - Windows: Uses `rundll32.exe user32.dll,LockWorkStation`
   - Immediately locks the PC

---

## Safety Features

### 5-Second Delay:
- Shutdown and restart have a 5-second delay
- Gives you time to cancel if needed
- Say "cancel shutdown" or "cancel restart" to stop

### Confirmation Messages:
- All commands provide voice feedback
- You know exactly what's happening
- Clear instructions on how to cancel

---

## Use Cases

### Scenario 1: Quick Cleanup
```
"Jarvis, close current window"
→ Closes unwanted window
"Jarvis, close current window"
→ Closes another window
```

### Scenario 2: End of Day
```
"Jarvis, lock PC"
→ Locks PC before leaving desk
```

### Scenario 3: Restart After Updates
```
"Jarvis, restart PC"
→ PC restarts in 5 seconds
```

### Scenario 4: Accidental Shutdown
```
"Jarvis, shutdown PC"
"Wait, I didn't save!"
"Jarvis, cancel shutdown"
→ Shutdown cancelled
```

---

## Platform Support

### Windows (Fully Supported):
- ✅ Close Window (Alt+F4)
- ✅ Shutdown (5 sec delay)
- ✅ Restart (5 sec delay)
- ✅ Cancel Shutdown/Restart
- ✅ Sleep
- ✅ Lock

### macOS (Supported):
- ✅ Close Window
- ✅ Shutdown (1 min delay)
- ✅ Restart (1 min delay)
- ✅ Cancel Shutdown/Restart
- ✅ Sleep
- ✅ Lock

### Linux (Supported):
- ✅ Close Window
- ✅ Shutdown (1 min delay)
- ✅ Restart (1 min delay)
- ✅ Cancel Shutdown/Restart
- ✅ Sleep
- ✅ Lock

---

## Important Warnings

### ⚠️ CRITICAL WARNINGS:

1. **Save Your Work:**
   - Always save before shutdown/restart
   - 5 seconds is not much time!
   - Use "cancel shutdown" if needed

2. **Close Window:**
   - Closes the ACTIVE window
   - Make sure the right window is focused
   - Unsaved work will be lost

3. **Lock PC:**
   - You'll need your password to unlock
   - Make sure you remember it!

4. **Sleep Mode:**
   - Unsaved work may be lost if battery dies
   - Save important work first

---

## Command Flow

### Example: Shutdown PC

1. **Voice Input:**
   ```
   "Jarvis, shutdown PC"
   ```

2. **Model Recognition:**
   ```
   Decision: ['system shutdown']
   ```

3. **Automation:**
   ```
   Processing command: system shutdown
   Calling: System('shutdown')
   ```

4. **Execution:**
   ```
   - Runs: shutdown /s /t 5
   - Returns: "Shutting down PC in 5 seconds sir..."
   ```

5. **Response:**
   ```
   Jarvis: "Shutting down PC in 5 seconds sir. Say cancel shutdown to stop."
   ```

6. **Result:**
   ```
   - PC shuts down in 5 seconds
   - Or cancelled if you say "cancel shutdown"
   ```

---

## Testing

### Test Close Window:
```python
from Backend.Automation import System

# Open notepad first
import subprocess
subprocess.Popen(['notepad.exe'])

# Wait a moment, then close it
import time
time.sleep(2)
result = System('close window')
print(result)  # "Closing current window sir"
```

### Test Shutdown (BE CAREFUL!):
```python
from Backend.Automation import System

# This will actually shutdown your PC!
# result = System('shutdown')
# print(result)

# To cancel:
# result = System('cancel shutdown')
# print(result)
```

---

## Troubleshooting

### Issue: Close window doesn't work
**Solutions:**
- Make sure a window is focused
- Try clicking on the window first
- Some system windows can't be closed

### Issue: Shutdown/Restart doesn't work
**Solutions:**
- Check if you have admin permissions
- Some systems require elevated privileges
- Try running Jarvis as administrator

### Issue: Can't cancel shutdown
**Solutions:**
- Say "cancel shutdown" quickly
- You have 5 seconds on Windows
- On Mac/Linux, you have more time

### Issue: Lock doesn't work
**Solutions:**
- Check if your system supports locking
- Verify you have a password set
- Try manually first to test

---

## Best Practices

### ✅ DO:
- Save your work before shutdown/restart
- Test commands with non-critical windows first
- Use "cancel shutdown" if you change your mind
- Lock PC when leaving your desk

### ❌ DON'T:
- Use shutdown without saving
- Close windows with unsaved work
- Forget your password before locking
- Use these commands carelessly

---

## Keyboard Shortcuts Used

| Command | Windows Shortcut | Action |
|---------|-----------------|--------|
| Close Window | Alt+F4 | Closes active window |
| Mute | Volume Mute Key | Mutes audio |
| Volume Up | Volume Up Key | Increases volume |
| Volume Down | Volume Down Key | Decreases volume |

---

## Command Reference

| Voice Command | System Command | Action | Delay |
|--------------|----------------|--------|-------|
| "close current window" | `system close window` | Closes window | Immediate |
| "shutdown pc" | `system shutdown` | Shuts down | 5 seconds |
| "restart pc" | `system restart` | Restarts | 5 seconds |
| "cancel shutdown" | `system cancel shutdown` | Cancels | Immediate |
| "sleep pc" | `system sleep` | Sleeps | Immediate |
| "lock pc" | `system lock` | Locks | Immediate |
| "mute" | `system mute` | Mutes | Immediate |
| "volume up" | `system volume up` | Increases | Immediate |

---

## Examples by Scenario

### Working from Home:
```
End of day:
"Jarvis, close current window"  (close work apps)
"Jarvis, lock PC"  (lock before leaving)
```

### Gaming:
```
"Jarvis, close current window"  (close game)
"Jarvis, sleep PC"  (save power)
```

### Maintenance:
```
"Jarvis, restart PC"  (after updates)
"Jarvis, cancel restart"  (if needed)
```

---

## Summary

Jarvis now has full system control capabilities:

✅ **Close Windows** - Close any active window
✅ **Shutdown** - Turn off your PC (with 5 sec delay)
✅ **Restart** - Reboot your PC (with 5 sec delay)
✅ **Cancel** - Stop shutdown/restart
✅ **Sleep** - Put PC to sleep mode
✅ **Lock** - Lock your PC
✅ **Volume** - Control system volume

🎉 **Feature Status: FULLY WORKING**

---

## Quick Reference

**Most Used Commands:**
1. "Jarvis, close current window"
2. "Jarvis, lock PC"
3. "Jarvis, shutdown PC"
4. "Jarvis, cancel shutdown"

**Remember:** Always save your work before using shutdown/restart! 🖥️
