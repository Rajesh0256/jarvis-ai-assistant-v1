# Search Features - Windows & Chrome

## Overview
Jarvis can now search in two different ways:
1. **Search in Windows** - Opens Windows search and finds files/folders
2. **Search in Chrome** - Opens Chrome browser and searches on Google

## Features

### 🔍 Search in Windows

**What it does:**
- Opens Windows search bar (Win + S)
- Types your search query automatically
- Searches for files, folders, apps, settings

**Usage:**
```
You: "Jarvis, search in windows for calculator"
Jarvis: "Searching for calculator in Windows sir"
Result: Windows search opens with "calculator" typed
```

**Examples:**
- "Search in windows for report.pdf"
- "Search in windows calculator"
- "Find in windows documents"
- "Search in windows chrome"
- "Look for notepad in windows"

---

### 🌐 Search in Chrome

**What it does:**
- Opens Google Chrome browser
- Searches your query on Google automatically
- Opens search results page

**Usage:**
```
You: "Jarvis, search in chrome python tutorial"
Jarvis: "Searching for python tutorial in Chrome sir"
Result: Chrome opens with Google search results for "python tutorial"
```

**Examples:**
- "Search in chrome weather today"
- "Search in chrome how to code"
- "Look up in chrome python tutorial"
- "Search in chrome best restaurants near me"
- "Find in chrome latest news"

---

## Command Formats

### Search in Windows

| Command | Result |
|---------|--------|
| "search in windows calculator" | Searches for calculator |
| "search in windows for report.pdf" | Searches for report.pdf |
| "find in windows documents" | Searches for documents |
| "search in windows chrome" | Searches for Chrome app |

### Search in Chrome

| Command | Result |
|---------|--------|
| "search in chrome python" | Google search for "python" |
| "search in chrome weather" | Google search for "weather" |
| "look up in chrome tutorials" | Google search for "tutorials" |
| "find in chrome news" | Google search for "news" |

---

## Differences

### Search in Windows vs Search in Chrome

| Feature | Search in Windows | Search in Chrome |
|---------|------------------|------------------|
| **Purpose** | Find files/folders/apps | Search the internet |
| **Opens** | Windows Search Bar | Chrome Browser |
| **Searches** | Local computer | Google (internet) |
| **Best for** | Files, apps, settings | Information, websites |

---

## Use Cases

### When to Use "Search in Windows"

✅ Finding files on your computer
✅ Looking for installed applications
✅ Searching for folders
✅ Finding system settings
✅ Locating documents

**Examples:**
- "Search in windows for my presentation"
- "Search in windows calculator"
- "Find in windows control panel"

### When to Use "Search in Chrome"

✅ Looking up information online
✅ Finding tutorials or guides
✅ Checking weather or news
✅ Researching topics
✅ Finding websites

**Examples:**
- "Search in chrome python tutorial"
- "Search in chrome weather forecast"
- "Look up in chrome how to cook pasta"

---

## Complete Workflow Examples

### Example 1: Find a File

```
You: "Jarvis, search in windows for report.pdf"

What happens:
1. Windows search bar opens (Win + S)
2. "report.pdf" is typed automatically
3. Windows shows matching files
4. You can click to open the file
```

### Example 2: Search Online

```
You: "Jarvis, search in chrome python tutorial"

What happens:
1. Chrome browser opens
2. Google search page loads
3. Search query "python tutorial" is entered
4. Search results appear
5. You can click on any result
```

### Example 3: Find an App

```
You: "Jarvis, search in windows calculator"

What happens:
1. Windows search opens
2. "calculator" is typed
3. Calculator app appears in results
4. You can click to open it
```

### Example 4: Research Topic

```
You: "Jarvis, search in chrome how to learn programming"

What happens:
1. Chrome opens
2. Google searches "how to learn programming"
3. Results show tutorials, courses, guides
4. You can browse and learn
```

---

## Technical Details

### Search in Windows Function

```python
def SearchInWindows(query):
    # Press Win + S to open search
    keyboard.press_and_release("win+s")
    # Wait for search to open
    time.sleep(0.8)
    # Type the query
    keyboard.write(query)
```

### Search in Chrome Function

```python
def SearchInChrome(query):
    # Find Chrome installation
    # Open Chrome with Google search URL
    search_url = f"https://www.google.com/search?q={query}"
    subprocess.Popen([chrome_path, search_url])
```

---

## Files Modified

1. **Backend/Automation.py**
   - Added `SearchInWindows()` function
   - Added `SearchInChrome()` function
   - Added command handlers

2. **Backend/Model.py**
   - Added "search in windows" to funcs
   - Added "search in chrome" to funcs
   - Added AI training examples

3. **Main.py**
   - Added commands to functions list

---

## Tips & Tricks

### For Windows Search

1. **Be Specific**: "search in windows report.pdf" is better than "search in windows report"
2. **Include Extensions**: Add .pdf, .docx, .txt for files
3. **Use App Names**: "calculator", "notepad", "chrome"
4. **Search Settings**: "control panel", "settings", "display"

### For Chrome Search

1. **Natural Language**: "how to", "what is", "best way to"
2. **Specific Topics**: Include keywords for better results
3. **Current Info**: Great for weather, news, time
4. **Learning**: Perfect for tutorials and guides

---

## Comparison with Other Search Commands

| Command | What it Does |
|---------|-------------|
| "search for calculator" | Opens Windows search (generic) |
| "search in windows calculator" | Opens Windows search (specific) |
| "search in chrome calculator" | Google search in Chrome |
| "google search calculator" | Opens Google in default browser |

---

## Testing

### Test Search in Windows

1. Say: "Jarvis, search in windows calculator"
2. Expected: Windows search opens with "calculator" typed
3. Result: Calculator app appears in results

### Test Search in Chrome

1. Say: "Jarvis, search in chrome python tutorial"
2. Expected: Chrome opens with Google search
3. Result: Search results for "python tutorial" appear

---

## Troubleshooting

### Windows Search Not Opening

- Check if Windows search is enabled
- Try pressing Win + S manually first
- Restart Jarvis

### Chrome Not Opening

- Check if Chrome is installed
- Verify Chrome path in code
- Try "open chrome" first to test

### Query Not Typing

- Check keyboard library is working
- Increase sleep time if needed
- Try manually to verify

---

## Status

✅ Search in Windows - Working
✅ Search in Chrome - Working
✅ Voice Commands - Working
✅ Speech Output - Working
✅ Both Features - Integrated

---

## Future Enhancements

- Search in Firefox
- Search in Edge
- Search in specific folders
- Advanced search filters
- Search history
- Quick search shortcuts

---

## Summary

You now have two powerful search features:

1. **Search in Windows** - Find files, apps, settings on your computer
2. **Search in Chrome** - Search the internet with Google

Both work seamlessly with voice commands and provide instant results! 🎉
