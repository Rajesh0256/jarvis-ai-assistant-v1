# Windows Search Feature Guide

## Overview
Jarvis can now open the Windows search bar and automatically type your search query.

## Voice Commands

### Basic Search
- "search for calculator"
- "search for notepad"
- "search for control panel"
- "search for settings"

### Alternative Command
- "windows search chrome"
- "windows search documents"

## How It Works
1. Jarvis presses Win+S to open Windows search
2. Waits 0.5 seconds for the search bar to open
3. Types your query automatically
4. You can then press Enter or click on results

## Examples

**Voice Command:** "Jarvis, search for calculator"
**Result:** Opens Windows search and types "calculator"

**Voice Command:** "Jarvis, search for my documents"
**Result:** Opens Windows search and types "my documents"

**Voice Command:** "Jarvis, search for control panel"
**Result:** Opens Windows search and types "control panel"

## Testing
Run the test script:
```bash
python test_windows_search.py
```

## Integration
The feature is integrated into Main.py and will work with your voice commands automatically.
