import sys
import subprocess
import threading
import json
import os
from asyncio import run
from time import sleep
from dotenv import dotenv_values

# Import threading at module level to avoid reimport warnings

# Fix paths for PyInstaller executable
if getattr(sys, 'frozen', False):
    # Running as compiled executable
    BASE_PATH = sys._MEIPASS
    os.chdir(os.path.dirname(sys.executable))
else:
    # Running as script
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

from Frontend.GUI import (
    GraphicalUserInterface,
    MainWindow,
    SetAsssistantStatus,
    ShowTextToScreen,
    TempDirectoryPath,
    SetMicrophoneStatus,
    AnswerModifier,
    QueryModifier,
    GetMicrophoneStatus,
    GetAssistantStatus,
)
from Frontend.LoginPage import LoginPage
from PyQt5.QtWidgets import QApplication
from Backend.Model import FirstLayerDMM
from Backend.RealtimeSearchEngine import RealtimeSearchEngine
from Backend.Automation import Automation
# Try to use fast speech recognition, fall back to original if not available
try:
    from Backend.FastSpeechToText import SpeechRecognition
    print("✅ Using Fast Speech Recognition (speech_recognition library)")
except ImportError:
    from Backend.SpeechToText import SpeechRecognition
    print("⚠️ Using Original Speech Recognition (Selenium)")
    print("💡 For faster response, install: pip install SpeechRecognition PyAudio")
from Backend.Chatbot import ChatBot
from Backend.TextToSpeech import TextToSpeech
from Backend.NewsGeopolitics import GetNews
from Backend.ReligionHistory import ReligionHistoryQuery

# Face Authentication removed

# Load environment variables
env_vars = dotenv_values(".env")
Username = env_vars.get("Username", "User")
Assistantname = env_vars.get("Assistantname", "Assistant")

DefaultMessage = f""" {Username}: Hello {Assistantname}, How are you?
{Assistantname}: Welcome {Username}. I am doing well. How may I help you? """

functions = ["open", "close", "play", "system", "content", "google search", "youtube search", "weather", 
             "open file", "open folder", "delete file", "delete folder", "create folder", 
             "search file", "find file", "file info", "show info", "rename file",
             "open recycle bin", "empty recycle bin", "recycle bin info", "select all",
             "fix error", "analyze error", "quick fix", "help with", "brightness", "search for", 
             "create app", "suggest language", "generate code", "generate in",
             "search in windows", "search in chrome", "delete selected files", "delete selected",
             "permanently delete selected", "news", "latest news", "current news", "geopolitics",
             "geopolitical", "world news", "international news", "religion", "religious", "faith",
             "history", "historical", "ancient", "civilization", "internet speed", "speed test",
             "check speed", "network speed", "analyze image", "read text from", "read image",
             "analyze screenshot", "analyze document", "summarize document", "find in image",
             "explain error", "what is this error"]
subprocess_list = []

# Quick acknowledgment responses for faster interaction
quick_responses = {
    "open": ["Opening sir", "On it sir", "Sure sir"],
    "close": ["Closing sir", "Done sir"],
    "play": ["Playing sir", "Sure sir"],
    "search": ["Searching sir", "On it sir"],
    "delete": ["Deleting sir", "Done sir"],
    "create": ["Creating sir", "Sure sir"],
}



# Ensure a default chat log exists if no chats are logged
def ShowDefaultChatIfNoChats():
    try:
        with open(r'Data\ChatLog.json', "r", encoding='utf-8') as file:
            if len(file.read()) < 5:
                with open(TempDirectoryPath('Database.data'), 'w', encoding='utf-8') as temp_file:
                    temp_file.write("")
                with open(TempDirectoryPath('Responses.data'), 'w', encoding='utf-8') as response_file:
                    response_file.write(DefaultMessage)
    except FileNotFoundError:
        print("ChatLog.json file not found. Creating default response.")
        os.makedirs("Data", exist_ok=True)
        with open(r'Data\ChatLog.json', "w", encoding='utf-8') as file:
            file.write("[]")
        with open(TempDirectoryPath('Responses.data'), 'w', encoding='utf-8') as response_file:
            response_file.write(DefaultMessage)

# Read chat log from JSON
def ReadChatLogJson():
    try:
        with open(r'Data\ChatLog.json', 'r', encoding='utf-8') as file:
            chatlog_data = json.load(file)
        return chatlog_data
    except FileNotFoundError:
        print("ChatLog.json not found.")
        return []

# Integrate chat logs into a readable format


def ChatLogIntegration():
    json_data = ReadChatLogJson()
    formatted_chatlog = ""
    for entry in json_data:
        if entry["role"] == "user":
            formatted_chatlog += f"{Username}: {entry['content']}\n"
        elif entry["role"] == "assistant":
            formatted_chatlog += f"{Assistantname}: {entry['content']}\n"

    # Ensure the Temp directory exists
    temp_dir_path = TempDirectoryPath('')  # Get the directory path
    if not os.path.exists(temp_dir_path):
        os.makedirs(temp_dir_path)

    with open(TempDirectoryPath('Database.data'), 'w', encoding='utf-8') as file:
        file.write(AnswerModifier(formatted_chatlog))

# Display the chat on the GUI
def ShowChatOnGUI():
    try:
        with open(TempDirectoryPath('Database.data'), 'r', encoding='utf-8') as file:
            data = file.read()
        if len(str(data)) > 0:
            with open(TempDirectoryPath('Responses.data'), 'w', encoding='utf-8') as response_file:
                response_file.write(data)
    except FileNotFoundError:
        print("Database.data file not found.")

# Quick decision function for common queries (faster than AI model)
def QuickDecision(query):
    """Fast pattern matching for common queries - bypasses AI model for speed"""
    import re
    
    # Clean up query - remove trailing punctuation
    query_lower = query.lower().strip().rstrip('.?!')
    
    # News patterns
    if re.search(r"what'?s? (?:the )?(?:latest |current )?news", query_lower):
        return ["news"]
    if re.search(r"tell me (?:the )?news", query_lower):
        return ["news"]
    if "geopolitic" in query_lower:
        return ["geopolitics"]
    if "world news" in query_lower or "international news" in query_lower:
        return ["world news"]
    
    # Religion patterns
    if re.search(r"tell me about (islam|muslim)", query_lower):
        return ["religion islam"]
    if re.search(r"tell me about (christianity|christian|jesus)", query_lower):
        return ["religion christianity"]
    if re.search(r"tell me about (hinduism|hindu)", query_lower):
        return ["religion hinduism"]
    if re.search(r"tell me about (buddhism|buddhist|buddha)", query_lower):
        return ["religion buddhism"]
    if re.search(r"tell me about (sikhism|sikh)", query_lower):
        return ["religion sikhism"]
    if "all.*religion" in query_lower or "major religion" in query_lower:
        return ["religion all religions"]
    
    # History patterns
    if "world war 2" in query_lower or "world war ii" in query_lower or "ww2" in query_lower:
        return ["history world war 2"]
    if "world war 1" in query_lower or "world war i" in query_lower or "ww1" in query_lower:
        return ["history world war 1"]
    if re.search(r"ancient (egypt|rome|greece|china|india)", query_lower):
        match = re.search(r"ancient (\w+)", query_lower)
        return [f"ancient {match.group(1)}"]
    if "indian independence" in query_lower:
        return ["history indian independence"]
    
    # Realtime patterns (current information)
    if re.search(r"who is (?:the )?(?:prime minister|pm) of india", query_lower):
        return ["realtime who is the prime minister of india"]
    if re.search(r"who is (?:the )?president of", query_lower):
        return ["realtime " + query]
    if re.search(r"what is (?:the )?capital of", query_lower):
        return ["realtime " + query]
    if "current" in query_lower and ("president" in query_lower or "prime minister" in query_lower):
        return ["realtime " + query]
    
    # Internet speed check
    if "internet speed" in query_lower or "speed test" in query_lower or "check speed" in query_lower or "network speed" in query_lower:
        return ["internet speed"]
    
    # Simple commands
    if query_lower.startswith("open "):
        app = query_lower.replace("open ", "").strip()
        return [f"open {app}"]
    if query_lower.startswith("close "):
        app = query_lower.replace("close ", "").strip()
        return [f"close {app}"]
    if query_lower.startswith("play "):
        song = query_lower.replace("play ", "").strip()
        return [f"play {song}"]
    
    # No quick match found - use AI model
    return None


# Initial execution setup
def InitialExecution():
    SetMicrophoneStatus("False")
    ShowTextToScreen("")
    ShowDefaultChatIfNoChats()
    ChatLogIntegration()
    ShowChatOnGUI()
    
    # Face authentication removed - using login page authentication instead
    SetAsssistantStatus("Available...")

# Main execution logic
def MainExecution(text_mode=False):
    try:
        TaskExecution = False
        ImageExecution = False
        ImageGenerationQuery = ""

        if text_mode:
            # Read from text input file
            SetAsssistantStatus("Processing text command...")
            print("📝 TEXT MODE: Reading from TextInput.data")
            try:
                text_file_path = TempDirectoryPath('TextInput.data')
                print(f"📝 TEXT MODE: File path: {text_file_path}")
                with open(text_file_path, 'r', encoding='utf-8') as file:
                    Query = file.read().strip()
                print(f"📝 TEXT MODE: Read command: '{Query}'")
                # Clear the text input file
                with open(text_file_path, 'w', encoding='utf-8') as file:
                    file.write("")
                print("📝 TEXT MODE: Cleared TextInput.data")
            except FileNotFoundError as e:
                print(f"❌ TEXT MODE: File not found: {e}")
                Query = ""
            except Exception as e:
                print(f"❌ TEXT MODE: Error reading file: {e}")
                Query = ""
        else:
            SetAsssistantStatus("Listening...")
            Query = SpeechRecognition()

        if not Query:
            print("⚠️ No query received, returning...")
            SetAsssistantStatus("Available...")
            return

        ShowTextToScreen(f"{Username}: {Query}")
        SetAsssistantStatus("Thinking...")
        
        # Quick pattern matching for faster response on common queries
        Decision = QuickDecision(Query)
        if Decision is None:
            # Fall back to AI decision model for complex queries
            Decision = FirstLayerDMM(Query)
        else:
            print(f"Quick Decision (Fast): {Decision}")

        print(f"\nDecision: {Decision}\n")

        G = any([i for i in Decision if i.startswith("general")])
        R = any([i for i in Decision if i.startswith("realtime")])


        Merged_query = " and ".join(
            [" ".join(i.split()[1:]) for i in Decision if i.startswith("general") or i.startswith("realtime")]
        )

        for queries in Decision:
            if "generate" in queries:
                ImageGenerationQuery = str(queries)
                ImageExecution = True

        for queries in Decision:
            if not TaskExecution:
                # Check for religion/history queries first
                if any(queries.startswith(keyword) for keyword in ["religion", "religious", "faith",
                                                                     "history", "historical", "ancient",
                                                                     "civilization"]):
                    SetAsssistantStatus("Thinking...")
                    # Extract the topic from the query
                    topic = queries.split(maxsplit=1)[1] if len(queries.split()) > 1 else queries
                    religion_history_result = ReligionHistoryQuery(topic)
                    # Display immediately
                    ShowTextToScreen(f"{Assistantname}: {religion_history_result}")
                    # Start speaking immediately (non-blocking)
                    SetAsssistantStatus("Answering...")
                    threading.Thread(target=TextToSpeech, args=(religion_history_result,), daemon=True).start()
                    return True
                
                # Check for news/geopolitics queries
                if any(queries.startswith(keyword) for keyword in ["news", "latest news", "current news", 
                                                                     "geopolitics", "geopolitical", 
                                                                     "world news", "international news"]):
                    SetAsssistantStatus("Fetching news...")
                    # Extract the topic from the query
                    topic = queries.split(maxsplit=1)[1] if len(queries.split()) > 1 else ""
                    news_result = GetNews(topic)
                    # Display immediately
                    ShowTextToScreen(f"{Assistantname}: {news_result}")
                    # Start speaking immediately (non-blocking)
                    SetAsssistantStatus("Answering...")
                    threading.Thread(target=TextToSpeech, args=(news_result,), daemon=True).start()
                    return True
                
                if any(queries.startswith(func) for func in functions):
                    # Give instant acknowledgment for faster feel (but not for create app)
                    import random
                    # Skip quick response for "create app" since we want full language suggestion
                    if not queries.startswith("create app") and not queries.startswith("suggest language"):
                        for key in quick_responses:
                            if queries.startswith(key):
                                quick_msg = random.choice(quick_responses[key])
                                SetAsssistantStatus("Working...")
                                # Start speaking immediately while processing
                                threading.Thread(target=TextToSpeech, args=(quick_msg,), daemon=True).start()
                                break
                    
                    automation_result = run(Automation(list(Decision)))
                    TaskExecution = True
                    # If automation returns a string (like personalized responses), display and speak it
                    if isinstance(automation_result, str) and automation_result != "True":
                        ShowTextToScreen(f"{Assistantname}: {automation_result}")
                        SetAsssistantStatus("Answering...")
                        # Always speak for create app, otherwise check if not already acknowledged
                        if queries.startswith("create app") or queries.startswith("suggest language"):
                            TextToSpeech(automation_result)
                        elif not any(queries.startswith(key) for key in quick_responses):
                            TextToSpeech(automation_result)
                        return True

        if ImageExecution:
            with open(r'Frontend\Files\ImageGeneration.data', "w") as file:
                file.write(f"{ImageGenerationQuery},True")

            try:
                p1 = subprocess.Popen(
                    ['python', r"Backend\ImageGeneration.py"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    stdin=subprocess.PIPE,
                    shell=False,
                )
                subprocess_list.append(p1)
            except Exception as e:
                print(f"Error starting ImageGeneration.py: {e}")

        if G and R or R:
            SetAsssistantStatus("Searching...")
            Answer = RealtimeSearchEngine(QueryModifier(Merged_query))
            ShowTextToScreen(f"{Assistantname}: {Answer}")
            SetAsssistantStatus("Answering...")
            # Start speaking immediately (non-blocking)
            threading.Thread(target=TextToSpeech, args=(Answer,), daemon=True).start()
            return True
        else:
            for queries in Decision:
                if "general" in queries:
                    SetAsssistantStatus("Thinking...")
                    QueryFinal = queries.replace("general", "")
                    Answer = ChatBot(QueryModifier(QueryFinal))
                    ShowTextToScreen(f"{Assistantname}: {Answer}")
                    SetAsssistantStatus("Answering...")
                    # Start speaking immediately (non-blocking)
                    threading.Thread(target=TextToSpeech, args=(Answer,), daemon=True).start()
                    return True
                elif "realtime" in queries:
                    SetAsssistantStatus("Searching...")
                    QueryFinal = queries.replace("realtime", "")
                    Answer = RealtimeSearchEngine(QueryModifier(QueryFinal))
                    ShowTextToScreen(f"{Assistantname}: {Answer}")
                    SetAsssistantStatus("Answering...")
                    # Start speaking immediately (non-blocking)
                    threading.Thread(target=TextToSpeech, args=(Answer,), daemon=True).start()
                    return True
                elif "exit" in queries:
                    QueryFinal = "Okay, Bye!"
                    Answer = ChatBot(QueryModifier(QueryFinal))
                    ShowTextToScreen(f"{Assistantname}: {Answer}")
                    SetAsssistantStatus("Answering...")
                    # For exit, speak synchronously to ensure it completes
                    TextToSpeech(Answer)
                    os._exit(1)
    except Exception as e:
        print(f"Error in MainExecution: {e}")

# Thread for primary execution loop
def FirstThread():
    while True:
        try:
            CurrentStatus = GetMicrophoneStatus()
            print(f"Current Microphone Status: {CurrentStatus}")  # Debugging

            if CurrentStatus.lower().strip() == "true":  # Voice command mode
                print("Executing MainExecution (Voice)")  # Debugging
                MainExecution(text_mode=False)
            elif CurrentStatus.lower().strip() == "text":  # Text command mode
                print("✅ TEXT MODE DETECTED!")  # Debugging
                print("Executing MainExecution (Text)")  # Debugging
                MainExecution(text_mode=True)
                # Reset status after processing text command
                SetMicrophoneStatus("False")
            elif CurrentStatus.lower() == "false":
                AIStatus = GetAssistantStatus()
                print(f"Current Assistant Status: {AIStatus}")  # Debugging

                if "Available..." in AIStatus:
                    sleep(0.1)
                else:
                    print("Setting Assistant Status to 'Available...'")  # Debugging
                    SetAsssistantStatus("Available...")
            else:
                print("Unexpected Microphone Status value. Defaulting to 'False'.")  # Debugging
        except Exception as e:
            print(f"Error in FirstThread: {e}")
            sleep(1)  # Avoid infinite rapid errors



# Entry point with authentication
def start_jarvis_with_auth():
    """Start Jarvis with login authentication"""
    app = QApplication(sys.argv)
    
    # Show login page
    login_page = LoginPage()
    login_page.setWindowTitle("Jarvis AI - Login")
    login_page.setFixedSize(600, 700)
    
    # Store references to prevent garbage collection
    authenticated_user = [None]
    main_window = [None]  # Store window reference
    
    def on_login_success(username):
        authenticated_user[0] = username
        login_page.close()
        print(f"\n{'='*60}")
        print(f"Welcome {username}! Starting Jarvis AI Assistant...")
        print(f"{'='*60}\n")
        
        # Start Jarvis after successful login
        InitialExecution()
        
        # Start the main execution thread
        thread1 = threading.Thread(target=FirstThread, daemon=True)
        thread1.start()
        
        # Show Jarvis GUI (reuse the same app instance)
        try:
            print("Creating Jarvis main window...")
            main_window[0] = MainWindow()  # Store in list to prevent garbage collection
            print("Showing Jarvis main window...")
            main_window[0].show()
            print("✅ Jarvis GUI is now visible!")
        except Exception as e:
            print(f"❌ Error starting Jarvis GUI: {e}")
            import traceback
            traceback.print_exc()
    
    login_page.login_successful.connect(on_login_success)
    login_page.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    # Start with authentication
    start_jarvis_with_auth()
    