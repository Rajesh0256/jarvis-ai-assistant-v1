# JARVIS AI ASSISTANT - USER MANUAL

## Welcome to Jarvis!

Jarvis is your intelligent AI assistant that can help you with tasks, answer questions, control your computer, and much more through voice commands.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Input Methods](#input-methods)
3. [Basic Commands](#basic-commands)
4. [Knowledge Features](#knowledge-features)
5. [Vision Features](#vision-features)
6. [File Operations](#file-operations)
7. [System Control](#system-control)
8. [Internet Features](#internet-features)
9. [Advanced Features](#advanced-features)
10. [Troubleshooting](#troubleshooting)

---

## Getting Started

### First Time Setup

1. **Start Jarvis**
   - Run `Main.py` or double-click the Jarvis launcher
   - Login with your credentials

2. **Activate Microphone**
   - Click the microphone button in the GUI
   - Wait for "Listening..." status

3. **Speak Your Command**
   - Speak clearly into your microphone
   - Wait for Jarvis to respond

4. **View Response**
   - Answer appears on screen
   - Jarvis speaks the response

### Basic Usage

1. Click microphone button
2. Speak your command
3. Wait for response
4. Repeat for next command

---

## Input Methods

### 🎤 Voice Input (Traditional)

**How to Use:**
1. Click the microphone button
2. Wait for "Listening..." status
3. Speak your command clearly
4. Jarvis processes and responds

**Best For:**
- Hands-free operation
- Quick simple commands
- Natural conversation
- Multitasking

**Example:**
- Say: "Open Chrome"
- Say: "What's the latest news?"
- Say: "Play music"

### 📝 Text Input (NEW!)

**How to Use:**
1. Find the text input field at the bottom of the screen
2. Type your command (e.g., "open notepad")
3. Press **Enter** or click **Send** button
4. Jarvis processes it just like voice commands

**Best For:**
- Quiet environments (library, office, public spaces)
- Complex commands with precise spelling
- Privacy (no audio recording)
- When microphone is unavailable
- Technical terms and file names

**Example:**
- Type: "open chrome"
- Type: "what's the latest news"
- Type: "create folder MyDocuments"

### 🔄 Switching Between Modes

**Voice to Text:**
1. Click in the text input field
2. Start typing your command
3. Press Enter to send

**Text to Voice:**
1. Click the microphone icon
2. Wait for "Listening..." status
3. Speak your command

**You can use both methods interchangeably - all features work with both!**

---

## Basic Commands

### Opening Applications

**Voice Commands:**
- "Open Chrome"
- "Open Notepad"
- "Open Calculator"
- "Open Facebook"
- "Open Instagram"

**What Jarvis Does:**
- Launches the requested application or website
- Confirms with "Opening sir"

### Closing Applications

**Voice Commands:**
- "Close Chrome"
- "Close Notepad"
- "Close Facebook"

**What Jarvis Does:**
- Closes the specified application
- Confirms with "Closing sir"

### Playing Music/Videos

**Voice Commands:**
- "Play [song name]"
- "Play Let It Go"
- "Play Despacito"

**What Jarvis Does:**
- Searches and plays the song on YouTube
- Confirms with "Playing sir"

### Opening Windows Folders

**Voice Commands:**
- "Open documents"
- "Open downloads"
- "Open pictures"
- "Open desktop"
- "Open videos"
- "Open music"

**What Jarvis Does:**
- Opens the specified Windows folder directly
- No need for full paths!

---

## Knowledge Features

### News & Current Events

**Voice Commands:**
- "What's the latest news?"
- "Tell me today's news"
- "Business news"
- "Technology news"
- "Sports news"
- "News about [topic]"

**What You Get:**
- Top 5 current headlines
- Source and date information
- Brief descriptions

**Setup (Optional):**
- Get free API key from https://newsapi.org/
- Add to .env: `NEWS_API_KEY=your_key`
- Restart Jarvis

### Geopolitics

**Voice Commands:**
- "Tell me about geopolitics"
- "What's happening in world politics?"
- "International relations"
- "World news"

**What You Get:**
- Current geopolitical updates
- International news
- Global affairs information

### Religion Knowledge

**Voice Commands:**
- "Tell me about Islam"
- "What is Christianity?"
- "Explain Hinduism"
- "Buddhist beliefs"
- "What are all the major religions?"
- "Tell me about Sikhism"

**What You Get:**
- Comprehensive information about 12+ religions
- Founders, holy books, beliefs, practices
- Respectful and objective information

**Religions Covered:**
- Christianity, Islam, Hinduism, Buddhism
- Sikhism, Judaism, Jainism, Zoroastrianism
- Shinto, Taoism, Confucianism, Bahá'í Faith

### History Knowledge

**Voice Commands:**
- "Tell me about World War 2"
- "Ancient Egypt"
- "Indian independence"
- "Roman Empire"
- "French Revolution"
- "Tell me about Napoleon"

**What You Get:**
- Detailed historical information
- Dates and timelines
- Important figures and events
- Context and significance

**History Covered:**
- Ancient civilizations (3000 BCE - 500 CE)
- Medieval period (500 - 1500 CE)
- Modern history (1500 - present)
- World Wars, revolutions, empires

### Realtime Information

**Voice Commands:**
- "Who is the Prime Minister of India?"
- "What is the capital of France?"
- "Who is the President of USA?"
- "Current population of China"

**What You Get:**
- Up-to-date, accurate information
- Current facts and figures
- Real-time data from web searches

---

## Vision Features

### Image Analysis

**Voice Commands:**
- "Analyze image C:\Photos\vacation.jpg"
- "What is in image [path]"
- "Describe this image [path]"

**What Jarvis Does:**
- Analyzes the image
- Describes what it sees
- Answers questions about the image

### Text Extraction (OCR)

**Voice Commands:**
- "Read text from C:\Screenshots\receipt.png"
- "Read image [path]"
- "What does this image say [path]"

**What Jarvis Does:**
- Extracts all text from the image
- Reads it back to you
- Maintains structure and formatting

**Use Cases:**
- Read receipts
- Extract text from scanned documents
- Convert images to text

### Screenshot Analysis

**Voice Commands:**
- "Analyze screenshot C:\Screenshots\desktop.png"
- "What does this screenshot show [path]"

**What Jarvis Does:**
- Analyzes the screenshot
- Explains UI elements
- Describes what's shown

### Document Analysis

**Voice Commands:**
- "Summarize document C:\Documents\contract.jpg"
- "Analyze document [path]"

**What Jarvis Does:**
- Reads the document
- Provides a summary
- Extracts key information

### Find Specific Information

**Voice Commands:**
- "Find due date in image C:\Bills\electric.jpg"
- "Find price in image C:\Receipts\shopping.png"
- "What is the phone number in [path]"

**What Jarvis Does:**
- Searches for the specific information
- Extracts and states it clearly
- Tells you if not found

### Error Message Explanation

**Voice Commands:**
- "Explain error C:\Screenshots\error.png"
- "What is this error [path]"
- "Help with error [path]"

**What Jarvis Does:**
- Reads the error message
- Explains what it means
- Suggests solutions

**Supported Formats:**
- JPG, JPEG, PNG, GIF, BMP, WEBP

---

## File Operations

### Opening Files

**Voice Commands:**
- "Open file report.pdf"
- "Open file C:\Documents\report.pdf"

**What Jarvis Does:**
- Opens the specified file
- Uses default application

### Opening Folders

**Voice Commands:**
- "Open folder projects"
- "Open folder C:\Work\Projects"

**What Jarvis Does:**
- Opens the folder in File Explorer

### Deleting Files/Folders

**Voice Commands:**
- "Delete file old_report.pdf"
- "Delete folder temp"

**What Jarvis Does:**
- Moves file/folder to Recycle Bin
- Confirms deletion

### Creating Folders

**Voice Commands:**
- "Create folder projects"
- "Create a new folder named work"

**What Jarvis Does:**
- Creates the folder
- Confirms creation

### Searching Files

**Voice Commands:**
- "Find file report.pdf"
- "Search for document.txt"

**What Jarvis Does:**
- Searches for the file
- Shows location if found

### File Information

**Voice Commands:**
- "Show info for report.pdf"
- "File info document.txt"

**What Jarvis Does:**
- Shows file size, date, location
- Provides file details

### Renaming Files

**Voice Commands:**
- "Rename file old.txt to new.txt"

**What Jarvis Does:**
- Renames the file
- Confirms the change

### Recycle Bin

**Voice Commands:**
- "Open recycle bin"
- "Empty recycle bin"
- "Recycle bin info"

**What Jarvis Does:**
- Opens/empties/shows info about Recycle Bin

### Select All Files

**Voice Commands:**
- "Select all files"
- "Select all"
- "Select all files in documents"

**What Jarvis Does:**
- Selects all files (Ctrl+A)
- Or selects all in specified folder

### Delete Selected Files

**Voice Commands:**
- "Delete selected files"
- "Delete all selected files"
- "Permanently delete selected files"

**What Jarvis Does:**
- Deletes currently selected files
- To Recycle Bin or permanently

---

## System Control

### Volume Control

**Voice Commands:**
- "Volume up"
- "Volume down"
- "Mute"
- "Unmute"

**What Jarvis Does:**
- Adjusts system volume
- Confirms the action

### Brightness Control

**Voice Commands:**
- "Increase brightness"
- "Decrease brightness"
- "Set brightness to 50"
- "Maximum brightness"
- "Minimum brightness"

**What Jarvis Does:**
- Adjusts screen brightness
- Confirms the level

### Window Management

**Voice Commands:**
- "Close current window"
- "Minimize window"

**What Jarvis Does:**
- Closes or minimizes active window

### Power Options

**Voice Commands:**
- "Shutdown PC"
- "Restart computer"
- "Lock PC"
- "Sleep PC"
- "Cancel shutdown"

**What Jarvis Does:**
- Executes the power command
- Confirms the action

---

## Internet Features

### Web Search

**Voice Commands:**
- "Google search Python tutorial"
- "Search for AI news"

**What Jarvis Does:**
- Opens Google with search results

### YouTube Search

**Voice Commands:**
- "YouTube search cooking recipes"
- "Search YouTube for music"

**What Jarvis Does:**
- Opens YouTube with search results

### Windows Search

**Voice Commands:**
- "Search in Windows for calculator"
- "Find in Windows report.pdf"

**What Jarvis Does:**
- Opens Windows search with query

### Chrome Search

**Voice Commands:**
- "Search in Chrome Python tutorial"
- "Look up in Chrome weather"

**What Jarvis Does:**
- Opens Chrome and searches

### Internet Speed Check

**Voice Commands:**
- "Check internet speed"
- "Test my internet speed"
- "Speed test"
- "Quick speed test"

**What You Get:**
- Download speed (Mbps)
- Ping/latency (ms)
- Connection quality rating

**Test Duration:**
- Full test: 10-15 seconds
- Quick test: 5-8 seconds

### Weather

**Voice Commands:**
- "What's the weather in New York?"
- "Weather in London"

**What Jarvis Does:**
- Provides weather information
- Current conditions

---

## Advanced Features

### Code Generation

**Voice Commands:**
- "Create a calculator app"
- "Generate code for to-do list"
- "Generate in Python for calculator"

**What Jarvis Does:**
- Suggests programming language
- Generates code
- Saves to file

### Error Fixing

**Voice Commands:**
- "Fix this error [error text]"
- "Analyze error [error message]"
- "Help with this error"

**What Jarvis Does:**
- Analyzes the error
- Suggests fixes
- Provides solutions

### Content Creation

**Voice Commands:**
- "Write a letter for sick leave"
- "Write an email about meeting"

**What Jarvis Does:**
- Generates the content
- Displays it for you

### Conversations

**Voice Commands:**
- "How are you?"
- "Tell me a joke"
- "What can you do?"
- "Chat with me"

**What Jarvis Does:**
- Engages in conversation
- Answers questions
- Provides information

---

## Tips for Best Results

### Speaking to Jarvis

1. **Speak Clearly**
   - Use normal speaking pace
   - Pronounce words clearly

2. **Be Specific**
   - "Open Chrome" not "Open browser"
   - "Delete file report.pdf" not "Delete that file"

3. **Use Full Paths**
   - For files: "C:\Documents\report.pdf"
   - Or relative: "Documents\report.pdf"

4. **Wait for Response**
   - Let Jarvis finish speaking
   - Wait for "Available..." status

### Common Patterns

**Opening Things:**
- "Open [app/website/folder]"

**Searching:**
- "Search for [query]"
- "Find [item]"

**Information:**
- "Tell me about [topic]"
- "What is [question]"

**Actions:**
- "Delete [item]"
- "Create [item]"
- "Close [app]"

---

## Troubleshooting

### Jarvis Not Responding

**Problem:** Microphone button clicked but nothing happens

**Solutions:**
1. Check microphone permissions
2. Ensure microphone is set as default device
3. Check if status shows "Listening..."
4. Try clicking microphone button again

### Speech Not Recognized

**Problem:** Jarvis doesn't understand what you said

**Solutions:**
1. Speak more clearly
2. Reduce background noise
3. Check microphone volume
4. Try rephrasing your command

### Slow Response

**Problem:** Jarvis takes long to respond

**Current Response Time:** 3-9 seconds

**To Make Faster:**
1. Install fast speech libraries:
   ```
   pip install SpeechRecognition PyAudio
   ```
2. Restart Jarvis
3. Response time reduces to 2-6 seconds

### Commands Not Working

**Problem:** Jarvis doesn't execute command

**Solutions:**
1. Check if command is supported (see this manual)
2. Use correct format (e.g., "Open Chrome" not "Launch Chrome")
3. For files, use full paths
4. Check if application is installed

### No Audio Output

**Problem:** Jarvis displays text but doesn't speak

**Solutions:**
1. Check speaker/headphone connection
2. Ensure volume is not muted
3. Check Windows audio settings
4. Restart Jarvis

---

## Quick Reference

### Most Common Commands

```
APPS:
  "Open Chrome"
  "Close Notepad"

FOLDERS:
  "Open documents"
  "Open downloads"

NEWS:
  "What's the latest news?"
  "Tell me about geopolitics"

KNOWLEDGE:
  "Tell me about Islam"
  "Tell me about World War 2"

REALTIME:
  "Who is the Prime Minister of India?"

VISION:
  "Read text from [image path]"
  "Analyze screenshot [path]"

FILES:
  "Delete file report.pdf"
  "Create folder projects"

SYSTEM:
  "Volume up"
  "Brightness increase"
  "Shutdown PC"

INTERNET:
  "Check internet speed"
  "Google search Python"
```

---

## Language Settings

### Current Language

Your Jarvis is configured for: **Hindi**

Settings in `.env`:
```
InputLanguage=hi-IN
AssistantVoice=hi-IN-MadhurNeural
```

### Change to English

Edit `.env` file:
```
InputLanguage=en-US
AssistantVoice=en-US-GuyNeural
```

Then restart Jarvis.

### Other Languages

Jarvis supports multiple languages. Change `InputLanguage` and `AssistantVoice` in `.env` to your preferred language.

---

## Configuration

### Environment Variables (.env)

```
Username=Master              # Your name
Assistantname=jarvis         # Assistant's name
InputLanguage=hi-IN          # Speech recognition language
AssistantVoice=hi-IN-MadhurNeural  # Text-to-speech voice
CohereAPIKey=your_key        # For decision making
GroqAPIKey=your_key          # For AI responses
GeminiAPIKey=your_key        # For image generation
NEWS_API_KEY=your_key        # For news (optional)
```

### Customization

**Change Assistant Name:**
1. Edit `.env` file
2. Change `Assistantname=jarvis` to your preferred name
3. Restart Jarvis

**Change Your Name:**
1. Edit `.env` file
2. Change `Username=Master` to your name
3. Restart Jarvis

---

## Performance

### Current Performance

**Response Times:**
- Simple commands: 2-4 seconds
- Knowledge queries: 3-6 seconds
- Complex queries: 5-9 seconds
- Vision analysis: 5-15 seconds

### Optimization Tips

1. **Install Fast Speech Recognition:**
   ```
   pip install SpeechRecognition PyAudio
   ```
   Reduces response time by 50%

2. **Use Quick Commands:**
   - Simple commands are faster
   - "Open Chrome" vs complex queries

3. **Clear Speech:**
   - Speak clearly for faster recognition
   - Reduce background noise

---

## All Features Summary

### ✅ What Jarvis Can Do

**KNOWLEDGE:**
- News & geopolitics
- 12+ world religions
- 5000+ years of history
- Current events
- General questions

**VISION:**
- Analyze images
- Read text (OCR)
- Understand screenshots
- Summarize documents
- Find information in images
- Explain error messages

**FILE OPERATIONS:**
- Open/close files and folders
- Delete files/folders
- Create folders
- Search files
- Rename files
- Recycle bin management
- Select all files

**SYSTEM CONTROL:**
- Volume control
- Brightness control
- Window management
- Power options (shutdown, restart, lock, sleep)

**INTERNET:**
- Web search (Google, YouTube)
- Windows search
- Chrome search
- Internet speed test

**APPLICATIONS:**
- Open/close any application
- Launch websites
- Play music/videos

**ADVANCED:**
- Code generation
- Error fixing
- Content creation
- Conversations

---

## Frequently Asked Questions

### Q: How do I activate Jarvis?
**A:** Click the microphone button in the GUI. Status will show "Listening..."

### Q: Can Jarvis understand Hindi?
**A:** Yes! Your Jarvis is configured for Hindi. It understands Hindi commands and responds in Hindi.

### Q: How do I make Jarvis faster?
**A:** Install SpeechRecognition and PyAudio libraries. See Performance section.

### Q: What image formats does Jarvis support?
**A:** JPG, JPEG, PNG, GIF, BMP, WEBP

### Q: Can Jarvis read handwritten text?
**A:** It can try, but works best with printed/typed text. Handwriting must be very clear.

### Q: How do I get news to work?
**A:** Get a free API key from newsapi.org and add it to .env file. Or use without API key for setup instructions.

### Q: Can Jarvis control my smart home devices?
**A:** Not currently. Jarvis focuses on computer control and information.

### Q: Is my data private?
**A:** Yes. Images and queries are processed securely. Nothing is stored permanently except your chat history locally.

### Q: Can I use Jarvis offline?
**A:** Partially. Most features require internet for AI processing. File operations and system control work offline.

### Q: How do I exit Jarvis?
**A:** Say "Bye Jarvis" or close the application window.

---

## Support & Documentation

### Quick Start Guides

- `START_HERE_NEWS_AND_REALTIME.txt` - News and realtime features
- `RELIGION_HISTORY_QUICK_START.txt` - Religion and history
- `VISION_QUICK_START.txt` - Vision features
- `INTERNET_SPEED_FEATURE.txt` - Speed test
- `QUICK_FIX_SLOW_RESPONSE.txt` - Performance tips

### Complete Guides

- `NEWS_GEOPOLITICS_GUIDE.md` - News features
- `RELIGION_HISTORY_GUIDE.md` - Religion and history
- `VISION_FEATURES_GUIDE.md` - Vision capabilities
- `RESPONSE_SPEED_OPTIMIZATION.md` - Speed optimization

### Feature Summaries

- `ALL_FEATURES_COMPLETE_SUMMARY.txt` - All features overview
- `COMPLETE_FEATURES_SUMMARY.txt` - Complete summary

---

## Version Information

**Current Version:** Enhanced Edition
**Last Updated:** December 2, 2025

**Recent Additions:**
- Vision analysis capabilities
- Religion knowledge (12+ religions)
- History knowledge (5000+ years)
- Internet speed check
- News & geopolitics
- Performance optimizations
- Llama 4 Scout model upgrade

---

## Contact & Credits

**Jarvis AI Assistant**
- Intelligent voice-controlled AI assistant
- Built with Python, PyQt5, Groq AI, Cohere
- Vision powered by Llama 3.2 Vision
- Responses powered by Llama 4 Scout

---

## Final Notes

### Remember:

1. **Speak clearly** for best recognition
2. **Be specific** in your commands
3. **Use full paths** for files and images
4. **Wait for response** before next command
5. **Check documentation** for detailed help

### Enjoy Jarvis!

Jarvis is designed to make your life easier. Explore all the features, experiment with commands, and discover how Jarvis can help you be more productive!

**Welcome to the future of AI assistance!** 🎉

---

*For technical support or feature requests, refer to the documentation files in the Jarvis directory.*
