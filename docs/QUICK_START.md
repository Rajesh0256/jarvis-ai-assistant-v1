# Jarvis Quick Start Guide

## 🚀 Getting Started in 3 Steps

### Step 1: Make Sure Everything is Installed
```bash
pip install -r Requirements.txt
```

### Step 2: Check Your .env File
Make sure you have these API keys:
```
Username=YourName
Assistantname=Jarvis
GroqAPIKey=your_groq_api_key
GeminiAPIKey=your_gemini_api_key
CohereAPIKey=your_cohere_api_key
InputLanguage=en
```

### Step 3: Run Jarvis
```bash
python Main.py
```

---

## 🎤 First Commands to Try

Once Jarvis is running, click the microphone button and try these:

### 1. Test Basic Conversation
```
"Jarvis, how are you?"
```
✅ Jarvis should respond with a greeting

### 2. Test Website Opening
```
"Jarvis, open Instagram"
```
✅ Instagram should open in your browser

### 3. Test Weather
```
"Jarvis, what's the weather in New York?"
```
✅ Jarvis should tell you the current weather

### 4. Test File Search
```
"Jarvis, find file document"
```
✅ Jarvis should search for files with "document" in the name

### 5. Test Folder Creation
```
"Jarvis, create folder test"
```
✅ A new folder called "test" should appear on your Desktop

---

## ✅ Verification Checklist

Run this test script to verify everything works:
```bash
python test_commands.py
```

You should see output like:
```
Input: 'open instagram'
Output: ['open instagram']
--------------------------------------------------
Input: 'what's the weather in New York'
Output: ['weather New York']
--------------------------------------------------
```

---

## 🎯 Most Useful Commands

### Quick Access to Websites
- "open Instagram"
- "open WhatsApp"
- "open Gmail"
- "open YouTube"

### File Management
- "find file [name]" - Search for files
- "open file [name]" - Open a file
- "create folder [name]" - Create new folder
- "show info for [filename]" - Get file details

### Information
- "weather in [city]" - Get weather
- "what's the time?" - Current time
- "google search [topic]" - Search Google

### Entertainment
- "play [song name]" - Play on YouTube
- "open Netflix" - Open Netflix
- "open Spotify" - Open Spotify

---

## 🔧 Troubleshooting

### Jarvis doesn't respond?
1. Check if microphone is working
2. Click the microphone button to activate
3. Speak clearly and wait for response

### Commands not working?
1. See COMMAND_EXAMPLES.md for correct format
2. Check TROUBLESHOOTING.md for solutions
3. Run test_commands.py to verify setup

### Can't find files?
- Files must be in: Desktop, Documents, Downloads, or Home folder
- Use specific file names with extensions
- Try: "find file [name]" first to locate it

---

## 📚 Documentation

- **COMMAND_EXAMPLES.md** - All available commands with examples
- **FILE_OPERATIONS_GUIDE.md** - Detailed file operation guide
- **TROUBLESHOOTING.md** - Solutions to common problems

---

## 🎓 Learning Path

### Day 1: Basic Commands
- Practice opening websites
- Try weather commands
- Test basic conversation

### Day 2: File Operations
- Search for files
- Open files and folders
- Create new folders

### Day 3: Advanced Features
- Content creation
- Multiple commands
- System controls

---

## 💡 Pro Tips

1. **Speak naturally** - Jarvis understands natural language
2. **Be specific** - Use full file names and locations
3. **Wait for response** - Give Jarvis time to process
4. **Check console** - Terminal shows what's happening
5. **Use examples** - Refer to COMMAND_EXAMPLES.md

---

## 🆘 Need Help?

1. **Check the guides:**
   - COMMAND_EXAMPLES.md
   - TROUBLESHOOTING.md
   - FILE_OPERATIONS_GUIDE.md

2. **Test individual components:**
   ```bash
   python test_commands.py
   ```

3. **Check console output:**
   - Look for error messages
   - See what commands are being processed

4. **Verify API keys:**
   - Make sure .env file has all keys
   - Keys should be valid and active

---

## 🎉 You're Ready!

Start with simple commands and gradually try more complex ones. Jarvis learns from your usage patterns and gets better over time.

**First command to try right now:**
```
"Jarvis, open Instagram"
```

Have fun! 🚀
