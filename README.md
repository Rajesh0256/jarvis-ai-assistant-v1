# 🤖 Jarvis AI Assistant

A powerful, feature-rich AI assistant with voice and text interaction capabilities, built with Python and powered by advanced AI models.

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)

## ✨ Features

### 🎤 Voice & Text Interaction
- **Voice Commands** - Speak naturally to Jarvis using advanced speech recognition
- **Text Input** - Type commands when voice isn't convenient
- **Text-to-Speech** - Natural voice responses with customizable voices
- **Fast Speech Recognition** - Quick response times for better user experience

### 🧠 AI-Powered Intelligence
- **Advanced Chatbot** - Powered by Groq and Google Generative AI
- **Context-Aware Responses** - Remembers conversation history
- **Personalized Interactions** - Adapts to your preferences
- **Error Fixing** - Analyzes and suggests fixes for code errors

### 🌐 Web & Information
- **Real-time Search** - Get instant answers from the web
- **News & Geopolitics** - Stay updated with latest news
- **Religion & History** - Access knowledge on various topics
- **Internet Speed Test** - Check your connection speed

### 🖥️ System Control
- **Brightness Control** - Adjust screen brightness with voice commands
- **Application Launcher** - Open apps hands-free
- **File Manager** - Create, delete, and manage files
- **Automation** - Automate repetitive tasks

### 🎨 Advanced Features
- **Image Generation** - Create images from text descriptions
- **Vision Analysis** - Analyze images and get AI insights
- **Background Mode** - Run Jarvis in the background with system tray
- **Floating Input Window** - Quick access input overlay
- **User Authentication** - Secure login system

## 📋 Requirements

- **Python**: 3.10, 3.11, or 3.12
- **Operating System**: Windows
- **API Keys**: Groq API and Google Generative AI API

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Rajesh0256/jarvis-ai-assistant-v1.git
cd jarvis-ai-assistant-v1
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r Requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

Get your API keys:
- Groq API: https://console.groq.com/
- Google AI: https://makersuite.google.com/app/apikey

### 5. Run Jarvis
```bash
python Main.py
```

## 📖 Usage

### Voice Commands Examples
- "Hello Jarvis" - Start conversation
- "What's the weather today?"
- "Open Chrome"
- "Set brightness to 50%"
- "Search for Python tutorials"
- "Tell me the latest news"
- "Create a file called test.txt"

### Text Input
Click the text input field in the GUI and type your commands when voice isn't suitable.

### Background Mode
Run `python Jarvis_Background.py` to start Jarvis in system tray mode with floating input window.

## 🏗️ Project Structure

```
jarvis-ai-assistant-v1/
├── Backend/              # Core functionality modules
│   ├── Chatbot.py       # AI conversation engine
│   ├── SpeechToText.py  # Voice recognition
│   ├── TextToSpeech.py  # Voice synthesis
│   └── ...
├── Frontend/            # GUI components
│   ├── GUI.py          # Main interface
│   ├── LoginPage.py    # Authentication
│   └── Graphics/       # UI assets
├── docs/               # Documentation
├── scripts/            # Utility scripts
├── Main.py            # Application entry point
└── Requirements.txt   # Dependencies
```

## 🔧 Building Executable

To create a standalone .exe file:

```bash
simple_build.bat
```

Or with console for debugging:
```bash
build_with_console.bat
```

See `BUILD_GUIDE.txt` for detailed instructions.

## 📚 Documentation

- [Publishing Guide](PUBLISHING_GUIDE.md) - How to publish and distribute
- [GitHub Setup Guide](GITHUB_SETUP_GUIDE.md) - Repository setup
- [Project Structure](PROJECT_STRUCTURE.md) - Detailed architecture
- [All Features](docs/ALL_FEATURES_SUMMARY.md) - Complete feature list

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Groq for fast AI inference
- Google Generative AI for advanced language models
- PyQt5 for the GUI framework
- All open-source contributors

## 📧 Contact

**Rajesh** - [@Rajesh0256](https://github.com/Rajesh0256)

Project Link: [https://github.com/Rajesh0256/jarvis-ai-assistant-v1](https://github.com/Rajesh0256/jarvis-ai-assistant-v1)

---

⭐ Star this repo if you find it helpful!
