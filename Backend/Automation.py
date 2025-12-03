from AppOpener import close, open as appopen
from webbrowser import open as webopen
from pywhatkit import search, playonyt
from dotenv import dotenv_values
from bs4 import BeautifulSoup
from rich import print
from groq import Groq
from Backend.FileManager import (
    OpenFileOrFolder,
    DeleteFileOrFolder,
    CreateFolder,
    SearchFiles,
    GetFileInfo,
    RenameFileOrFolder,
    CopyFileOrFolder,
    MoveFileOrFolder,
    OpenRecycleBin,
    EmptyRecycleBin,
    GetRecycleBinInfo,
    SelectAllFilesInFolder
)
from Backend.ErrorFixer import ErrorFixer, analyze_error_from_text
from Backend.BrightnessControl import (
    SetBrightness,
    IncreaseBrightness,
    DecreaseBrightness,
    GetCurrentBrightness,
    MaxBrightness,
    MinBrightness,
    MediumBrightness
)
from Backend.InternetSpeed import CheckInternetSpeed, CheckInternetSpeedQuick
from Backend.VisionAnalysis import (
    AnalyzeImage,
    ReadTextFromImage,
    AnalyzeScreenshot,
    AnalyzeDocument,
    FindInformationInImage,
    ExplainErrorMessage
)
from Backend.ApplicationLauncher import ApplicationLauncher
import webbrowser
import subprocess
import requests
import keyboard
import asyncio
import os

# Initialize Application Launcher
app_launcher = ApplicationLauncher()

env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey")

classes = ["zCubwf", "hgKELc", "LTKOO SY7ric", "ZOLcW", "gsrt vk_bk FzvWSb YwPhnf", "pclqee", "tw-Data-text tw-text-small tw-ta",
           "IZ6rdc", "05uR6d LTKOO", "vlzY6d", "webanswers-webanswers_table_webanswers-table", "dDoNo ikb4Bb gsrt", "sXLa0e", 
           "LWkfKe", "VQF4g", "qv3Wpe", "kno-rdesc", "SPZz6b"]

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

# Initialize Groq client only if API key exists
client = None
if GroqAPIKey:
    client = Groq(api_key=GroqAPIKey)

professional_responses = [
    "Your satisfaction is my top priority; feel free to reach out if there's anything else I can help you with.",
    "I'm at your service for any additional questions or support you may need—don't hesitate to ask.",
]

messages = []

SystemChatBot = [{"role": "system", "content": f"Hello, I am {os.environ.get('Username', 'User')}, a content writer. You have to write content like letters, codes, applications, essays, notes, songs, poems, etc."}]


def GoogleSearch(topic):
    search(topic)
    return True


def Content(topic):
    def OpenNotepad(file):
        try:
            default_text_editor = 'notepad.exe'
            subprocess.Popen([default_text_editor, file])
            return True
        except Exception as e:
            print(f"Error opening notepad: {e}")
            return False

    def ContentWriterAI(prompt):
        if not client:
            print("Error: Groq API key not found. Please check your .env file.")
            return "Error: Unable to generate content - API key missing."
        
        try:
            messages.append({"role": "user", "content": f"{prompt}"})

            completion = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=SystemChatBot + messages,
                max_tokens=2048,
                temperature=0.7,
                top_p=1,
                stream=True,
                stop=None
            )

            answer = ""

            for chunk in completion:
                if chunk.choices[0].delta.content:
                    answer += chunk.choices[0].delta.content

            answer = answer.replace("</s>", "")
            messages.append({"role": "assistant", "content": answer})
            return answer
        except Exception as e:
            print(f"Error generating content: {e}")
            return f"Error: Unable to generate content - {str(e)}"

    topic = topic.replace("content", "").strip()
    content_by_ai = ContentWriterAI(topic)

    # Create Data directory if it doesn't exist
    data_dir = "Data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created directory: {data_dir}")

    filepath = os.path.join(data_dir, f"{topic.lower().replace(' ', '_')}.txt")
    
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content_by_ai)
        print(f"Content written to: {filepath}")
        
        OpenNotepad(filepath)
        return True
    except Exception as e:
        print(f"Error writing content to file: {e}")
        return False

# Content("write A application for sick leave")
def YouTubeSearch(topic):
    url = f"https://www.youtube.com/results?search_query={topic}"
    webbrowser.open(url)
    return True


def PlayYoutube(query):
    try:
        playonyt(query)
        return True
    except Exception as e:
        print(f"Error playing YouTube video: {e}")
        return False


# Assuming `AppOpener` and `webopen` are defined or imported
import webbrowser
import requests
from bs4 import BeautifulSoup
import subprocess
import os
import platform

import webbrowser
import requests
from bs4 import BeautifulSoup
import subprocess
import os
import platform

def OpenApp(app, sess=requests.session()):
    
    # Special handling for common browsers
    app_lower = app.lower()
    
    if "chrome" in app_lower:
        try:
            # Try to open Chrome directly
            chrome_paths = [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe")
            ]
            
            for chrome_path in chrome_paths:
                if os.path.exists(chrome_path):
                    subprocess.Popen([chrome_path])
                    return f"Chrome opening sir"
            
            # If Chrome not found in standard locations, try AppOpener
            appopen("chrome", match_closest=False, output=True, throw_error=True)
            return f"Chrome opening sir"
        except:
            # Fallback to opening Chrome website
            webbrowser.open("https://www.google.com/chrome/")
            return f"Chrome opening sir"
    
    try:
        # Try to open the app using AppOpener
        appopen(app, match_closest=True, output=True, throw_error=True)
        return f"{app} opening sir"

    except:
        def extract_links(html):
            if html is None:
                return []
            soup = BeautifulSoup(html, 'html.parser')
            # Find all anchors with valid href attributes
            links = soup.find_all('a', href=True)
            return [link.get('href') for link in links]
            
        def search_google(query):
            url = f"https://www.microsoft.com/en-us/search?q={query}"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
            response = sess.get(url, headers=headers)
            if response.status_code == 200:
                return response.text
            else:
                print("Failed to retrieve search results.")
                return None

        def open_in_chrome_beta(url):
            """Open URL specifically in Google Chrome Beta"""
            system = platform.system()
            
            try:
                if system == "Windows":
                    # Common Chrome Beta paths on Windows
                    chrome_beta_paths = [
                        r"C:\Program Files\Google\Chrome Beta\Application\chrome.exe",
                        r"C:\Program Files (x86)\Google\Chrome Beta\Application\chrome.exe",
                        os.path.expanduser(r"~\AppData\Local\Google\Chrome Beta\Application\chrome.exe")
                    ]
                    
                    for path in chrome_beta_paths:
                        if os.path.exists(path):
                            subprocess.run([path, url])
                            return True
                    
                    # Fallback to regular Chrome if Beta not found
                    chrome_stable_paths = [
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                        os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe")
                    ]
                    
                    for path in chrome_stable_paths:
                        if os.path.exists(path):
                            print("Chrome Beta not found, using stable Chrome")
                            subprocess.run([path, url])
                            return True
                
                elif system == "Darwin":  # macOS
                    # Try Chrome Beta first
                    try:
                        subprocess.run(["open", "-a", "Google Chrome Beta", url])
                        return True
                    except:
                        print("Chrome Beta not found, trying stable Chrome")
                        subprocess.run(["open", "-a", "Google Chrome", url])
                        return True
                
                elif system == "Linux":
                    # Try Chrome Beta first
                    try:
                        subprocess.run(["google-chrome-beta", url])
                        return True
                    except:
                        print("Chrome Beta not found, trying stable Chrome")
                        subprocess.run(["google-chrome", url])
                        return True
                
                # Final fallback to default browser
                print("Chrome Beta and stable Chrome not found, opening in default browser")
                webbrowser.open(url)
                return True
                
            except Exception as e:
                print(f"Error opening Chrome Beta: {e}")
                # Final fallback
                webbrowser.open(url)
                return True

        # Attempt a search for the app
        html = search_google(app)
        if html:
            links = extract_links(html)
            if links:
                link = links[0]
                open_in_chrome_beta(link)
        return f"{app} opening sir"
# OpenApp("instagram")
def CloseApp(app):
    if "chrome" in app.lower():
        try:
            subprocess.run(["taskkill", "/f", "/im", "chrome.exe"], check=True)
            print(f"Closed Chrome using taskkill")
            return True
        except:
            pass
    
    try:
        close(app, match_closest=True, output=True, throw_error=True)
        print(f"Closed {app} using AppOpener")
        return True
    except Exception as e:
        print(f"Error closing {app}: {e}")
        return False


def GetWeather(location):
    """Get weather information for a specific location"""
    try:
        # Using wttr.in API - a simple weather service
        url = f"https://wttr.in/{location}?format=%C+%t+%h+%w"
        headers = {"User-Agent": useragent}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            weather_data = response.text.strip()
            # Format: Condition Temperature Humidity Wind
            return f"Weather in {location}: {weather_data}"
        else:
            return f"Sorry, I couldn't fetch weather information for {location}."
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return f"Sorry, I couldn't fetch weather information for {location}."


def WindowsSearch(query):
    """Open Windows search bar with a query"""
    try:
        # Press Windows key + S to open search
        keyboard.press_and_release("win+s")
        # Wait a moment for search to open
        import time
        time.sleep(0.5)
        # Type the query
        keyboard.write(query)
        return f"Searching for {query} in Windows sir"
    except Exception as e:
        print(f"Error opening Windows search: {e}")
        return f"Sorry, I couldn't open Windows search sir"


def SearchInWindows(query):
    """Search for files/folders in Windows search"""
    try:
        # Press Windows key + S to open search
        keyboard.press_and_release("win+s")
        # Wait a moment for search to open
        import time
        time.sleep(0.8)
        # Type the query
        keyboard.write(query)
        return f"Searching for {query} in Windows sir"
    except Exception as e:
        print(f"Error searching in Windows: {e}")
        return f"Sorry, I couldn't search in Windows sir"


def SearchInChrome(query):
    """Open Chrome and search for a topic"""
    try:
        # First, open Chrome
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe")
        ]
        
        chrome_found = False
        for chrome_path in chrome_paths:
            if os.path.exists(chrome_path):
                # Open Chrome with Google search URL
                search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
                subprocess.Popen([chrome_path, search_url])
                chrome_found = True
                break
        
        if not chrome_found:
            # Fallback to default browser
            search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(search_url)
        
        return f"Searching for {query} in Chrome sir"
    except Exception as e:
        print(f"Error searching in Chrome: {e}")
        return f"Sorry, I couldn't search in Chrome sir"


def DeleteSelectedFiles():
    """Delete all currently selected files in File Explorer"""
    try:
        import time
        
        # Press Delete key to delete selected files
        keyboard.press_and_release("delete")
        
        # Wait a moment for delete confirmation dialog
        time.sleep(0.3)
        
        # Press Enter to confirm deletion (moves to Recycle Bin)
        keyboard.press_and_release("enter")
        
        return "Deleted all selected files sir"
    except Exception as e:
        print(f"Error deleting selected files: {e}")
        return f"Sorry, I couldn't delete the selected files sir"


def DeleteSelectedFilesPermanently():
    """Permanently delete all currently selected files (bypass Recycle Bin)"""
    try:
        import time
        
        # Press Shift + Delete for permanent deletion
        keyboard.press_and_release("shift+delete")
        
        # Wait for confirmation dialog
        time.sleep(0.3)
        
        # Press Enter to confirm permanent deletion
        keyboard.press_and_release("enter")
        
        return "Permanently deleted all selected files sir"
    except Exception as e:
        print(f"Error permanently deleting selected files: {e}")
        return f"Sorry, I couldn't permanently delete the selected files sir"


def SelectAllFilesInCurrentFolder():
    """Select all files in the currently open folder using Ctrl+A"""
    try:
        # Press Ctrl + A to select all
        keyboard.press_and_release("ctrl+a")
        
        return "Selected all files in the current folder sir"
    except Exception as e:
        print(f"Error selecting all files: {e}")
        return f"Sorry, I couldn't select all files sir"


def handle_brightness_command(command):
    """Handle brightness control commands"""
    import re
    
    command_lower = command.lower()
    
    try:
        # Check for specific brightness levels
        if "maximum" in command_lower or "max" in command_lower or "full" in command_lower:
            success, msg = MaxBrightness()
            return msg if success else "Failed to set maximum brightness sir"
        
        elif "minimum" in command_lower or "min" in command_lower or "lowest" in command_lower:
            success, msg = MinBrightness()
            return msg if success else "Failed to set minimum brightness sir"
        
        elif "medium" in command_lower or "mid" in command_lower or "half" in command_lower:
            success, msg = MediumBrightness()
            return msg if success else "Failed to set medium brightness sir"
        
        elif "increase" in command_lower or "up" in command_lower or "raise" in command_lower or "higher" in command_lower:
            # Check for specific amount
            numbers = re.findall(r'\d+', command)
            amount = int(numbers[0]) if numbers else 10
            success, msg = IncreaseBrightness(amount)
            return msg if success else "Failed to increase brightness sir"
        
        elif "decrease" in command_lower or "down" in command_lower or "lower" in command_lower or "reduce" in command_lower:
            # Check for specific amount
            numbers = re.findall(r'\d+', command)
            amount = int(numbers[0]) if numbers else 10
            success, msg = DecreaseBrightness(amount)
            return msg if success else "Failed to decrease brightness sir"
        
        else:
            # Check for specific percentage
            numbers = re.findall(r'\d+', command)
            if numbers:
                level = int(numbers[0])
                if 0 <= level <= 100:
                    success, msg = SetBrightness(level)
                    return msg if success else f"Failed to set brightness to {level} percent sir"
                else:
                    return "Brightness level must be between 0 and 100 percent sir"
            else:
                # Get current brightness
                current = GetCurrentBrightness()
                if current is not None:
                    return f"Current brightness is {current} percent sir"
                else:
                    return "Could not get current brightness sir"
    
    except Exception as e:
        print(f"Error handling brightness command: {e}")
        return "Sorry, I couldn't control the brightness sir"


def System(command):
    def mute():
        keyboard.press_and_release("volume mute")

    def unmute():
        keyboard.press_and_release("volume mute")

    def volume_up():
        keyboard.press_and_release("volume up")

    def volume_down():
        keyboard.press_and_release("volume down")
    
    def close_window():
        """Close the current active window"""
        keyboard.press_and_release("alt+f4")
        return "Closing current window sir"
    
    def shutdown_pc():
        """Shutdown the PC"""
        if platform.system() == "Windows":
            subprocess.run(["shutdown", "/s", "/t", "5"], check=False)
            return "Shutting down PC in 5 seconds sir. Say cancel shutdown to stop."
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["sudo", "shutdown", "-h", "+1"], check=False)
            return "Shutting down PC in 1 minute sir"
        else:  # Linux
            subprocess.run(["shutdown", "-h", "+1"], check=False)
            return "Shutting down PC in 1 minute sir"
    
    def restart_pc():
        """Restart the PC"""
        if platform.system() == "Windows":
            subprocess.run(["shutdown", "/r", "/t", "5"], check=False)
            return "Restarting PC in 5 seconds sir. Say cancel restart to stop."
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["sudo", "shutdown", "-r", "+1"], check=False)
            return "Restarting PC in 1 minute sir"
        else:  # Linux
            subprocess.run(["shutdown", "-r", "+1"], check=False)
            return "Restarting PC in 1 minute sir"
    
    def cancel_shutdown():
        """Cancel scheduled shutdown/restart"""
        if platform.system() == "Windows":
            subprocess.run(["shutdown", "/a"], check=False)
            return "Shutdown cancelled sir"
        else:
            subprocess.run(["sudo", "shutdown", "-c"], check=False)
            return "Shutdown cancelled sir"
    
    def sleep_pc():
        """Put PC to sleep"""
        if platform.system() == "Windows":
            subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState", "0,1,0"], check=False)
            return "Putting PC to sleep sir"
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["pmset", "sleepnow"], check=False)
            return "Putting PC to sleep sir"
        else:  # Linux
            subprocess.run(["systemctl", "suspend"], check=False)
            return "Putting PC to sleep sir"
    
    def lock_pc():
        """Lock the PC"""
        if platform.system() == "Windows":
            subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"], check=False)
            return "Locking PC sir"
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["/System/Library/CoreServices/Menu Extras/User.menu/Contents/Resources/CGSession", "-suspend"], check=False)
            return "Locking PC sir"
        else:  # Linux
            subprocess.run(["xdg-screensaver", "lock"], check=False)
            return "Locking PC sir"

    try:
        if command == "mute":
            mute()
            return "Muted sir"
        elif command == "unmute":
            unmute()
            return "Unmuted sir"
        elif command == "volume up":
            volume_up()
            return "Volume increased sir"
        elif command == "volume down":
            volume_down()
            return "Volume decreased sir"
        elif command == "close window" or command == "close current window":
            return close_window()
        elif command == "shutdown" or command == "shutdown pc":
            return shutdown_pc()
        elif command == "restart" or command == "restart pc":
            return restart_pc()
        elif command == "cancel shutdown" or command == "cancel restart":
            return cancel_shutdown()
        elif command == "sleep" or command == "sleep pc":
            return sleep_pc()
        elif command == "lock" or command == "lock pc":
            return lock_pc()
        # Brightness controls
        elif "brightness" in command:
            return handle_brightness_command(command)
        # Internet speed check
        elif "internet speed" in command or "speed test" in command or "check speed" in command:
            return "Checking internet speed sir. This may take a moment..."
        else:
            print(f"Unknown system command: {command}")
            return f"Unknown system command: {command}"
        
    except Exception as e:
        print(f"Error executing system command {command}: {e}")
        return f"Error executing system command: {str(e)}"


def FixError(error_text):
    """Analyze and fix Python errors"""
    try:
        print(f"Analyzing error: {error_text[:100]}...")
        result = analyze_error_from_text(error_text)
        return result
    except Exception as e:
        return f"Error analyzing: {str(e)}"


def FixErrorFromFile(filepath):
    """Analyze error from a log file"""
    try:
        if not os.path.exists(filepath):
            return f"File not found: {filepath}"
        
        with open(filepath, 'r', encoding='utf-8') as f:
            error_text = f.read()
        
        return FixError(error_text)
    except Exception as e:
        return f"Error reading file: {str(e)}"


def QuickErrorFix(error_type):
    """Get quick fix for common error types"""
    fixer = ErrorFixer()
    
    quick_fixes = {
        "module not found": "Install the missing module using: pip install [module_name]",
        "import error": "Reinstall the package: pip install --upgrade --force-reinstall [package]",
        "syntax error": "Check for missing colons, brackets, or quotes in your code",
        "indentation": "Use consistent indentation (4 spaces or tabs, not both)",
        "name error": "Make sure the variable is defined before using it",
        "attribute error": "Check if the object has that attribute/method",
        "type error": "Convert variables to compatible types",
        "value error": "Validate input before conversion",
        "file not found": "Check if the file path is correct",
        "key error": "Use dictionary.get('key', default) to avoid KeyError",
    }
    
    error_type_lower = error_type.lower()
    for key, fix in quick_fixes.items():
        if key in error_type_lower:
            return f"Quick fix for {error_type}:\n{fix}"
    
    return "Please provide the full error message for detailed analysis"


def SuggestLanguageForApp(app_name):
    """Suggest programming languages for creating different types of applications"""
    app_name_lower = app_name.lower()
    
    # Define language suggestions based on application type
    suggestions = {
        "calculator": {
            "languages": ["Python", "JavaScript", "Java", "C++"],
            "recommendation": "Python",
            "reason": "Python is great for quick calculator apps with libraries like Tkinter for GUI"
        },
        "website": {
            "languages": ["HTML/CSS/JavaScript", "React", "Vue.js", "Angular"],
            "recommendation": "HTML/CSS/JavaScript",
            "reason": "These are the fundamental web technologies for building websites"
        },
        "web app": {
            "languages": ["JavaScript (Node.js)", "Python (Django/Flask)", "Java (Spring)", "PHP"],
            "recommendation": "JavaScript with Node.js",
            "reason": "Node.js is popular for modern web applications with great ecosystem"
        },
        "mobile app": {
            "languages": ["React Native", "Flutter (Dart)", "Swift (iOS)", "Kotlin (Android)"],
            "recommendation": "Flutter",
            "reason": "Flutter allows you to build for both iOS and Android with one codebase"
        },
        "game": {
            "languages": ["C#", "C++", "Python", "JavaScript"],
            "recommendation": "C# with Unity",
            "reason": "Unity with C# is excellent for both 2D and 3D game development"
        },
        "desktop app": {
            "languages": ["Python", "Java", "C#", "Electron (JavaScript)"],
            "recommendation": "Python",
            "reason": "Python with PyQt or Tkinter makes desktop app development straightforward"
        },
        "ai": {
            "languages": ["Python", "R", "Julia"],
            "recommendation": "Python",
            "reason": "Python has the best AI/ML libraries like TensorFlow, PyTorch, and scikit-learn"
        },
        "machine learning": {
            "languages": ["Python", "R", "Julia"],
            "recommendation": "Python",
            "reason": "Python dominates ML with libraries like TensorFlow, PyTorch, and scikit-learn"
        },
        "chatbot": {
            "languages": ["Python", "JavaScript", "Java"],
            "recommendation": "Python",
            "reason": "Python has excellent NLP libraries and frameworks for chatbot development"
        },
        "api": {
            "languages": ["Python (Flask/FastAPI)", "Node.js (Express)", "Java (Spring)", "Go"],
            "recommendation": "Python with FastAPI",
            "reason": "FastAPI is modern, fast, and easy to use for building APIs"
        },
        "database": {
            "languages": ["SQL", "Python", "Java"],
            "recommendation": "SQL",
            "reason": "SQL is essential for database management and queries"
        },
        "automation": {
            "languages": ["Python", "Bash", "PowerShell"],
            "recommendation": "Python",
            "reason": "Python is perfect for automation with simple syntax and powerful libraries"
        },
        "todo": {
            "languages": ["Python", "JavaScript", "Java", "C#"],
            "recommendation": "Python",
            "reason": "Python makes it easy to create todo apps with GUI or web frameworks"
        },
        "note": {
            "languages": ["Python", "JavaScript", "Java"],
            "recommendation": "Python",
            "reason": "Python with Tkinter or web frameworks is great for note-taking apps"
        },
        "music player": {
            "languages": ["Python", "Java", "C++", "JavaScript"],
            "recommendation": "Python",
            "reason": "Python has libraries like pygame and tkinter for music player development"
        },
        "video player": {
            "languages": ["Python", "C++", "Java"],
            "recommendation": "Python",
            "reason": "Python with libraries like VLC or OpenCV can handle video playback"
        },
    }
    
    # Find matching application type
    for app_type, info in suggestions.items():
        if app_type in app_name_lower:
            languages_list = ", ".join(info["languages"])
            response = (
                f"For creating a {app_name}, I suggest these languages: {languages_list}. "
                f"My recommendation is {info['recommendation']} because {info['reason']}. "
                f"Would you like me to help you get started sir?"
            )
            return response
    
    # Default suggestion if no specific match
    return (
        f"For creating a {app_name}, I recommend starting with Python for its simplicity and versatility, "
        f"or JavaScript if it's a web-based application. Python is great for beginners and has extensive libraries. "
        f"JavaScript is essential for web development. Would you like me to help you get started sir?"
    )


def GenerateAppCode(app_name, language="Python"):
    """Generate code for the requested application in specified language"""
    if not client:
        return "Error: Groq API key not found. Please check your .env file."
    
    try:
        prompt = f"""Generate a complete, working {language} code for a {app_name}. 
        
Requirements:
- Write clean, well-commented code
- Include all necessary imports
- Make it functional and ready to run
- For GUI apps, use appropriate libraries (Tkinter for Python, etc.)
- Add error handling
- Keep it simple but complete

Generate ONLY the code, no explanations before or after."""

        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {"role": "system", "content": "You are an expert programmer. Generate clean, working code."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=3000,
            temperature=0.7,
        )

        code = completion.choices[0].message.content
        code = code.replace("```python", "").replace("```javascript", "").replace("```java", "")
        code = code.replace("```cpp", "").replace("```html", "").replace("```", "").strip()
        
        return code
    except Exception as e:
        print(f"Error generating code: {e}")
        return f"Error generating code: {str(e)}"


def CreateApp(app_description):
    """Handle app creation requests by suggesting languages and generating code"""
    # Remove "create" or "create a" from the beginning
    app_name = app_description.replace("create a ", "").replace("create ", "").strip()
    
    # Get language suggestions
    suggestion = SuggestLanguageForApp(app_name)
    
    # Add prompt to generate code
    suggestion += "\n\nWould you like me to generate the code for you? Just say 'yes' or specify the language like 'generate in Python' sir."
    
    return suggestion


def GenerateAndSaveCode(app_name, language="Python"):
    """Generate code and save it to a file"""
    print(f"Generating {language} code for {app_name}...")
    
    # Generate the code
    code = GenerateAppCode(app_name, language)
    
    if code.startswith("Error"):
        return code
    
    # Determine file extension
    extensions = {
        "python": ".py",
        "javascript": ".js",
        "java": ".java",
        "c++": ".cpp",
        "html": ".html",
        "css": ".css",
    }
    
    ext = extensions.get(language.lower(), ".txt")
    
    # Create Data directory if it doesn't exist
    data_dir = "Data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # Save the code
    filename = f"{app_name.lower().replace(' ', '_')}{ext}"
    filepath = os.path.join(data_dir, filename)
    
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(code)
        print(f"Code saved to: {filepath}")
        
        # Open in notepad
        try:
            default_text_editor = 'notepad.exe'
            subprocess.Popen([default_text_editor, filepath])
        except Exception as e:
            print(f"Error opening file: {e}")
        
        return f"I've generated the {language} code for your {app_name} and saved it to {filename}. The file is now open sir."
    except Exception as e:
        print(f"Error saving code: {e}")
        return f"Error saving code: {str(e)}"


async def TranslateAndExecute(commands: list[str]):
    funcs = []

    for command in commands:
        print(f"Processing command: {command}")
        
        # Check for recycle bin commands first (before general "open")
        if command.startswith("open recycle bin") or command.startswith("open trash"):
            fun = asyncio.to_thread(OpenRecycleBin)
            funcs.append(fun)
        elif command.startswith("open file ") or command.startswith("open folder "):
            # File/folder open operation
            name = command.replace("open file ", "").replace("open folder ", "").strip()
            fun = asyncio.to_thread(OpenFileOrFolder, name)
            funcs.append(fun)
        elif command.startswith("open "):
            app_name = command.removeprefix("open ").strip().rstrip('.?!')
            
            # Check for common Windows folders first
            windows_folders = {
                'documents': os.path.expanduser('~\\Documents'),
                'downloads': os.path.expanduser('~\\Downloads'),
                'pictures': os.path.expanduser('~\\Pictures'),
                'videos': os.path.expanduser('~\\Videos'),
                'music': os.path.expanduser('~\\Music'),
                'desktop': os.path.expanduser('~\\Desktop'),
                'download': os.path.expanduser('~\\Downloads'),  # Alias
                'document': os.path.expanduser('~\\Documents'),  # Alias
                'picture': os.path.expanduser('~\\Pictures'),  # Alias
                'video': os.path.expanduser('~\\Videos'),  # Alias
            }
            
            app_name_lower = app_name.lower().replace(' folder', '').replace(' ', '').rstrip('.?!')
            
            if app_name_lower in windows_folders:
                # Open the Windows folder directly
                folder_path = windows_folders[app_name_lower]
                fun = asyncio.to_thread(OpenFileOrFolder, folder_path)
                funcs.append(fun)
            elif any(ext in app_name.lower() for ext in ['.pdf', '.txt', '.doc', '.xls', '.ppt', '.jpg', '.png', '.mp4', '.mp3']):
                # It's likely a file
                fun = asyncio.to_thread(OpenFileOrFolder, app_name)
                funcs.append(fun)
            else:
                # It's an app or website
                fun = asyncio.to_thread(OpenApp, app_name)
                funcs.append(fun)
        elif command.startswith("delete selected files permanently") or command.startswith("permanently delete selected"):
            # Permanently delete selected files (Shift+Delete) - MUST be before generic "delete"
            fun = asyncio.to_thread(DeleteSelectedFilesPermanently)
            funcs.append(fun)
        elif command.startswith("delete selected files") or command.startswith("delete selected") or command.startswith("delete all selected"):
            # Delete selected files (to Recycle Bin) - MUST be before generic "delete"
            fun = asyncio.to_thread(DeleteSelectedFiles)
            funcs.append(fun)
        elif command.startswith("delete file ") or command.startswith("delete folder ") or command.startswith("delete "):
            name = command.replace("delete file ", "").replace("delete folder ", "").replace("delete ", "").strip()
            fun = asyncio.to_thread(DeleteFileOrFolder, name, True)
            funcs.append(fun)
        elif command.startswith("generate code ") or command.startswith("generate in "):
            # Handle code generation requests
            parts = command.replace("generate code ", "").replace("generate in ", "").strip()
            # Parse: "generate in Python for calculator" or "generate code calculator in Python"
            if " for " in parts:
                language, app_name = parts.split(" for ", 1)
            elif " in " in parts:
                app_name, language = parts.split(" in ", 1)
            else:
                # Default to Python if no language specified
                app_name = parts
                language = "Python"
            fun = asyncio.to_thread(GenerateAndSaveCode, app_name.strip(), language.strip())
            funcs.append(fun)
        elif command.startswith("create app ") or command.startswith("suggest language "):
            # Handle app creation requests with language suggestions (MUST be before "create folder")
            app_name = command.replace("create app ", "").replace("suggest language ", "").strip()
            fun = asyncio.to_thread(CreateApp, f"create {app_name}")
            funcs.append(fun)
        elif command.startswith("create folder ") or command.startswith("create "):
            folder_name = command.replace("create folder ", "").replace("create ", "").strip()
            fun = asyncio.to_thread(CreateFolder, folder_name)
            funcs.append(fun)
        elif command.startswith("search in windows "):
            # Search specifically in Windows search (MUST be before generic "search")
            query = command.replace("search in windows ", "").strip()
            fun = asyncio.to_thread(SearchInWindows, query)
            funcs.append(fun)
        elif command.startswith("search in chrome "):
            # Search specifically in Chrome browser (MUST be before generic "search")
            query = command.replace("search in chrome ", "").strip()
            fun = asyncio.to_thread(SearchInChrome, query)
            funcs.append(fun)
        elif command.startswith("select all files") or command == "select all":
            # Select all files in current folder (Ctrl+A)
            fun = asyncio.to_thread(SelectAllFilesInCurrentFolder)
            funcs.append(fun)
        elif command.startswith("search file ") or command.startswith("find file ") or command.startswith("find ") or command.startswith("search "):
            name = command.replace("search file ", "").replace("find file ", "").replace("find ", "").replace("search ", "").strip()
            fun = asyncio.to_thread(SearchFiles, name)
            funcs.append(fun)
        elif command.startswith("file info ") or command.startswith("show info ") or command.startswith("info "):
            name = command.replace("file info ", "").replace("show info ", "").replace("info ", "").strip()
            fun = asyncio.to_thread(GetFileInfo, name)
            funcs.append(fun)
        elif command.startswith("rename file "):
            parts = command.removeprefix("rename file ").strip().split(" to ")
            if len(parts) == 2:
                fun = asyncio.to_thread(RenameFileOrFolder, parts[0].strip(), parts[1].strip())
                funcs.append(fun)
        elif command.startswith("select all ") or command.startswith("select all files "):
            folder_name = command.replace("select all files in ", "").replace("select all in ", "").replace("select all ", "").strip()
            fun = asyncio.to_thread(SelectAllFilesInFolder, folder_name)
            funcs.append(fun)
        elif command.startswith("close "):
            app_name = command.removeprefix("close ").strip()
            fun = asyncio.to_thread(CloseApp, app_name)
            funcs.append(fun)
        elif command.startswith("play "):
            query = command.removeprefix("play ").strip()
            fun = asyncio.to_thread(PlayYoutube, query)
            funcs.append(fun)
        elif command.startswith("content "):
            topic = command.removeprefix("content ").strip()
            fun = asyncio.to_thread(Content, topic)
            funcs.append(fun)
        elif command.startswith("google search "):
            query = command.removeprefix("google search ").strip()
            fun = asyncio.to_thread(GoogleSearch, query)
            funcs.append(fun)
        elif command.startswith("youtube search "):
            query = command.removeprefix("youtube search ").strip()
            fun = asyncio.to_thread(YouTubeSearch, query)
            funcs.append(fun)
        elif command.startswith("system "):
            sys_command = command.removeprefix("system ").strip()
            fun = asyncio.to_thread(System, sys_command)
            funcs.append(fun)
        elif command.startswith("weather "):
            location = command.removeprefix("weather ").strip()
            fun = asyncio.to_thread(GetWeather, location)
            funcs.append(fun)
        elif "internet speed" in command or "speed test" in command or "check speed" in command or "network speed" in command:
            # Internet speed test
            if "quick" in command:
                fun = asyncio.to_thread(CheckInternetSpeedQuick)
            else:
                fun = asyncio.to_thread(CheckInternetSpeed)
            funcs.append(fun)
        elif command.startswith("analyze image ") or command.startswith("what is in image "):
            # Image analysis
            image_path = command.replace("analyze image ", "").replace("what is in image ", "").strip()
            fun = asyncio.to_thread(AnalyzeImage, image_path)
            funcs.append(fun)
        elif command.startswith("read text from ") or command.startswith("read image "):
            # OCR - Read text from image
            image_path = command.replace("read text from ", "").replace("read image ", "").strip()
            fun = asyncio.to_thread(ReadTextFromImage, image_path)
            funcs.append(fun)
        elif command.startswith("analyze screenshot "):
            # Screenshot analysis
            image_path = command.replace("analyze screenshot ", "").strip()
            fun = asyncio.to_thread(AnalyzeScreenshot, image_path)
            funcs.append(fun)
        elif command.startswith("analyze document ") or command.startswith("summarize document "):
            # Document analysis
            image_path = command.replace("analyze document ", "").replace("summarize document ", "").strip()
            fun = asyncio.to_thread(AnalyzeDocument, image_path)
            funcs.append(fun)
        elif command.startswith("find ") and " in image " in command:
            # Find specific information in image
            parts = command.split(" in image ")
            info_type = parts[0].replace("find ", "").strip()
            image_path = parts[1].strip()
            fun = asyncio.to_thread(FindInformationInImage, image_path, info_type)
            funcs.append(fun)
        elif command.startswith("explain error ") or command.startswith("what is this error "):
            # Explain error message in image
            image_path = command.replace("explain error ", "").replace("what is this error ", "").strip()
            fun = asyncio.to_thread(ExplainErrorMessage, image_path)
            funcs.append(fun)
        elif command.startswith("search for ") or command.startswith("windows search "):
            query = command.replace("search for ", "").replace("windows search ", "").strip()
            fun = asyncio.to_thread(WindowsSearch, query)
            funcs.append(fun)
        elif command.startswith("empty recycle bin") or command.startswith("empty trash") or command.startswith("clear recycle bin"):
            fun = asyncio.to_thread(EmptyRecycleBin)
            funcs.append(fun)
        elif command.startswith("recycle bin info") or command.startswith("trash info"):
            fun = asyncio.to_thread(GetRecycleBinInfo)
            funcs.append(fun)
        elif command.startswith("fix error ") or command.startswith("analyze error "):
            error_text = command.replace("fix error ", "").replace("analyze error ", "").strip()
            fun = asyncio.to_thread(FixError, error_text)
            funcs.append(fun)
        elif command.startswith("fix error from file ") or command.startswith("analyze error file "):
            filepath = command.replace("fix error from file ", "").replace("analyze error file ", "").strip()
            fun = asyncio.to_thread(FixErrorFromFile, filepath)
            funcs.append(fun)
        elif command.startswith("quick fix ") or command.startswith("help with "):
            error_type = command.replace("quick fix ", "").replace("help with ", "").strip()
            fun = asyncio.to_thread(QuickErrorFix, error_type)
            funcs.append(fun)
        else:
            print(f"No function found for command: {command}")

    if funcs:
        results = await asyncio.gather(*funcs, return_exceptions=True)
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                print(f"Command {i+1} failed with exception: {result}")
            else:
                print(f"Command {i+1} result: {result}")
            yield result
    else:
        print("No valid commands to execute")


async def Automation(commands: list[str]):
    print(f"Starting automation with commands: {commands}")
    results = []
    text_results = []
    
    async for result in TranslateAndExecute(commands):
        results.append(result)
        # Collect text results (weather, file operations, etc.)
        if isinstance(result, str) and any(keyword in result for keyword in [
            "Weather in", "Opening", "opening", "deleted", "Deleted", "Created", "found", 
            "information:", "renamed", "copied", "moved", "couldn't find",
            "Recycle Bin", "emptied", "contains", "Trash", "selected", "Selected", "sir",
            "Closing", "Shutting", "Restarting", "cancelled", "sleep", "Locking",
            "Muted", "Unmuted", "Volume", "Brightness", "brightness", "percent",
            "Searching", "suggest", "languages", "recommendation", "creating",
            "generated", "code", "saved", "file is now open", "search", "Chrome",
            "Permanently"
        ]):
            text_results.append(result)
    
    print(f"Automation completed. Results: {results}")
    
    # Return text results if any, otherwise return True
    if text_results:
        return "\n".join(text_results)
    return True


# if __name__ == "__main__":
#     # Test with some commands
#     test_commands = [
#         "open notepad", 
#         " content application for sick leave"
#     ]
    
#     print("Testing automation...")
#     asyncio.run(Automation(test_commands))