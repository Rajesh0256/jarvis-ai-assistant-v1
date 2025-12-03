# 💡 Jarvis Brightness Control Feature

## Overview
Jarvis can now control your system's brightness level using voice commands!

---

## 🎯 Voice Commands

### Set Specific Brightness Level
- "Set brightness to 50 percent"
- "Set brightness to 75"
- "Brightness 30 percent"
- "Make brightness 80"

### Increase Brightness
- "Increase brightness"
- "Brightness up"
- "Raise brightness"
- "Make it brighter"
- "Increase brightness by 20" (specific amount)

### Decrease Brightness
- "Decrease brightness"
- "Brightness down"
- "Lower brightness"
- "Make it darker"
- "Reduce brightness"
- "Decrease brightness by 15" (specific amount)

### Preset Levels
- "Maximum brightness" / "Max brightness" / "Full brightness"
- "Minimum brightness" / "Min brightness" / "Lowest brightness"
- "Medium brightness" / "Half brightness" / "Mid brightness"

### Check Current Level
- "What is the brightness"
- "Current brightness"
- "Check brightness"

---

## 📋 Examples

### Example 1: Set to 50%
**You:** "Jarvis, set brightness to 50 percent"
**Jarvis:** "Brightness set to 50 percent"

### Example 2: Increase
**You:** "Jarvis, increase brightness"
**Jarvis:** "Brightness set to 60 percent"

### Example 3: Maximum
**You:** "Jarvis, maximum brightness"
**Jarvis:** "Brightness set to 100 percent"

### Example 4: Specific Increase
**You:** "Jarvis, increase brightness by 25"
**Jarvis:** "Brightness set to 85 percent"

---

## 🔧 How It Works

### Technical Details
- Uses Windows WMI (Windows Management Instrumentation)
- Controls monitor brightness directly
- Works on laptops and monitors with brightness control
- Range: 0-100%
- Default increment/decrement: 10%

### Requirements
- Windows operating system
- Laptop or monitor with brightness control support
- Administrator privileges (for some systems)

---

## 🚀 Quick Start

### Test Brightness Control
```bash
python test_brightness.py
```

This will:
1. Show current brightness
2. Let you test different commands
3. Verify brightness control works

### Use with Jarvis
```bash
python Main.py
```

Then say any brightness command!

---

## 💡 Tips

### Best Practices
1. **Start with medium brightness** - Easier on eyes
2. **Use presets** - Faster than specific numbers
3. **Gradual changes** - Increase/decrease by 10-20% at a time
4. **Check current level** - Before making changes

### Common Use Cases
- **Morning:** "Maximum brightness" (bright environment)
- **Evening:** "Set brightness to 30" (reduce eye strain)
- **Battery saving:** "Minimum brightness"
- **Presentations:** "Full brightness"
- **Night mode:** "Set brightness to 20"

---

## 🔍 Troubleshooting

### Issue: "Could not get current brightness"
**Possible Causes:**
- Not a laptop or brightness-capable monitor
- Brightness control not supported by hardware
- Driver issues

**Solutions:**
- Check if manual brightness control works (Fn keys)
- Update display drivers
- Try running as administrator

### Issue: "Failed to set brightness"
**Possible Causes:**
- Insufficient permissions
- Hardware doesn't support software brightness control
- WMI service not running

**Solutions:**
- Run Jarvis as administrator
- Check Windows services (WMI should be running)
- Restart computer

### Issue: Brightness changes but not to exact level
**Cause:** Some hardware only supports specific brightness steps

**Solution:** This is normal - hardware limitation

---

## 🎨 Integration

### In Your Code
```python
from Backend.BrightnessControl import (
    SetBrightness,
    IncreaseBrightness,
    DecreaseBrightness,
    GetCurrentBrightness
)

# Set to 50%
success, msg = SetBrightness(50)

# Increase by 10%
success, msg = IncreaseBrightness(10)

# Get current level
current = GetCurrentBrightness()
print(f"Current: {current}%")
```

### Voice Command Processing
Brightness commands are automatically detected when you say:
- "brightness" keyword
- Followed by action (increase, decrease, set, etc.)
- Optional: specific number

---

## 📊 Command Reference

| Command Type | Example | Result |
|-------------|---------|--------|
| Set Level | "brightness 50" | Sets to 50% |
| Increase | "brightness up" | Increases by 10% |
| Decrease | "brightness down" | Decreases by 10% |
| Maximum | "max brightness" | Sets to 100% |
| Minimum | "min brightness" | Sets to 0% |
| Medium | "medium brightness" | Sets to 50% |
| Check | "current brightness" | Reports current level |

---

## 🔐 Permissions

### Windows UAC
Some systems may require administrator privileges:

1. Right-click Jarvis executable
2. Select "Run as administrator"
3. Or: Set compatibility mode to always run as admin

### Alternative
If admin access is an issue, use keyboard shortcuts:
- Most laptops: Fn + Brightness keys
- Jarvis can simulate these keypresses

---

## 🎯 Advanced Features

### Custom Brightness Profiles
Create presets for different scenarios:

```python
# Morning profile
SetBrightness(100)

# Work profile
SetBrightness(70)

# Evening profile
SetBrightness(40)

# Night profile
SetBrightness(20)
```

### Automatic Brightness
Combine with time-based automation:
- Morning (6 AM - 12 PM): 80-100%
- Afternoon (12 PM - 6 PM): 60-80%
- Evening (6 PM - 10 PM): 30-50%
- Night (10 PM - 6 AM): 10-30%

---

## ✅ Success Indicators

When brightness control is working:
- ✅ `test_brightness.py` shows current brightness
- ✅ Voice commands change brightness immediately
- ✅ Jarvis confirms with "Brightness set to X percent"
- ✅ Screen brightness visibly changes

---

## 📚 Related Features

Jarvis also controls:
- 🔊 Volume (up, down, mute)
- 🔒 System (lock, sleep, shutdown)
- 🪟 Windows (close, minimize)
- 📁 Files (open, close, manage)

---

## 🎉 Examples in Action

### Scenario 1: Starting Work
**You:** "Jarvis, maximum brightness"
**Jarvis:** "Brightness set to 100 percent"

### Scenario 2: Battery Saving
**You:** "Jarvis, set brightness to 30"
**Jarvis:** "Brightness set to 30 percent"

### Scenario 3: Gradual Adjustment
**You:** "Jarvis, decrease brightness by 20"
**Jarvis:** "Brightness set to 50 percent"

### Scenario 4: Quick Check
**You:** "Jarvis, what's the brightness"
**Jarvis:** "Current brightness is 50 percent sir"

---

**Your Jarvis can now control brightness! Try it out!** 💡✨
