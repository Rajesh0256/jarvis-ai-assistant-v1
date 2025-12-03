"""Jarvis AI Assistant - Background Mode Launcher"""
import sys
import os
import threading
from time import sleep

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from Backend.BackgroundMode import BackgroundMode
from Frontend.GUI import (
    GraphicalUserInterface,
    SetAsssistantStatus,
    ShowTextToScreen,
    SetMicrophoneStatus,
    GetMicrophoneStatus,
    TempDirectoryPath,
)
from Frontend.FloatingInput import FloatingInputWindow
from Backend.SpeechToText import SpeechRecognition
from Backend.Model import FirstLayerDMM
from Backend.Automation import Automation
from Backend.Chatbot import ChatBot
from Backend.TextToSpeech import TextToSpeech
from Backend.RealtimeSearchEngine import RealtimeSearchEngine
from dotenv import dotenv_values
from asyncio import run
from PyQt5.QtWidgets import QApplication

# Load environment variables
env_vars = dotenv_values(".env")
Username = env_vars.get("Username", "User")
Assistantname = env_vars.get("Assistantname", "Jarvis")

# Global variables
background_mode = None
gui_window = None
floating_input = None
is_listening = False


def monitor_text_input():
    """Monitor for text input commands"""
    print("🔵 Text input monitor started")
    
    while True:
        try:
            # Check microphone status
            status = GetMicrophoneStatus()
            
            if status.strip().lower() == "text":
                print("✅ TEXT MODE DETECTED in background!")
                
                # Read text command
                try:
                    with open(TempDirectoryPath('TextInput.data'), 'r', encoding='utf-8') as file:
                        query = file.read().strip()
                    
                    if query:
                        print(f"📝 Text command: '{query}'")
                        ShowTextToScreen(f"{Username}: {query}")
                        
                        # Process the query
                        SetAsssistantStatus("Thinking...")
                        decision = FirstLayerDMM(query)
                        
                        print(f"Decision: {decision}")
                        
                        # Execute automation or chatbot
                        functions = ["open", "close", "play", "system", "content"]
                        task_executed = False
                        
                        for queries in decision:
                            if any(queries.startswith(func) for func in functions):
                                automation_result = run(Automation(list(decision)))
                                task_executed = True
                                break
                        
                        if not task_executed:
                            # Use chatbot
                            for queries in decision:
                                if "general" in queries:
                                    answer = ChatBot(queries.replace("general", ""))
                                    ShowTextToScreen(f"{Assistantname}: {answer}")
                                    TextToSpeech(answer)
                                    break
                                elif "realtime" in queries:
                                    answer = RealtimeSearchEngine(queries.replace("realtime", ""))
                                    ShowTextToScreen(f"{Assistantname}: {answer}")
                                    TextToSpeech(answer)
                                    break
                        
                        # Clear text input file
                        with open(TempDirectoryPath('TextInput.data'), 'w', encoding='utf-8') as file:
                            file.write("")
                    
                    # Reset status
                    SetMicrophoneStatus("False")
                    SetAsssistantStatus("Available...")
                    
                except Exception as e:
                    print(f"❌ Error processing text command: {e}")
                    SetMicrophoneStatus("False")
            
            sleep(0.1)  # Check every 100ms
            
        except Exception as e:
            print(f"❌ Error in text monitor: {e}")
            sleep(1)


def start_floating_input():
    """Start the floating text input window"""
    global floating_input
    
    try:
        # Create QApplication if not exists
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        
        # Create floating input window
        floating_input = FloatingInputWindow()
        floating_input.show()
        
        print("✅ Floating text input window started")
        print("   You can now type commands in the floating window!")
        
        # Keep the window running
        if app:
            app.exec_()
            
    except Exception as e:
        print(f"❌ Error starting floating input: {e}")


def activate_jarvis():
    """Called when Jarvis is activated via hotkey or tray icon"""
    global is_listening
    
    print("\n" + "="*60)
    print("🎤 JARVIS ACTIVATED")
    print("="*60)
    
    # Show notification
    if background_mode:
        background_mode.show_notification(
            "Jarvis Activated",
            "Listening for your command..."
        )
    
    # Set listening status
    is_listening = True
    SetMicrophoneStatus("True")
    SetAsssistantStatus("Listening...")
    
    try:
        # Get voice input
        query = SpeechRecognition()
        
        if query:
            print(f"\n{Username}: {query}")
            ShowTextToScreen(f"{Username}: {query}")
            
            # Process the query
            SetAsssistantStatus("Thinking...")
            decision = FirstLayerDMM(query)
            
            print(f"Decision: {decision}")
            
            # Check for automation tasks
            functions = ["open", "close", "play", "system", "content", 
                        "google search", "youtube search", "weather",
                        "open file", "open folder", "delete file", 
                        "delete folder", "create folder", "search file"]
            
            task_executed = False
            for queries in decision:
                if any(queries.startswith(func) for func in functions):
                    automation_result = run(Automation(list(decision)))
                    task_executed = True
                    if isinstance(automation_result, str) and automation_result != "True":
                        ShowTextToScreen(f"{Assistantname}: {automation_result}")
                        SetAsssistantStatus("Answering...")
                        TextToSpeech(automation_result)
                        break
            
            if not task_executed:
                # Check for general or realtime queries
                for queries in decision:
                    if "general" in queries:
                        SetAsssistantStatus("Thinking...")
                        query_final = queries.replace("general", "")
                        answer = ChatBot(query_final)
                        ShowTextToScreen(f"{Assistantname}: {answer}")
                        SetAsssistantStatus("Answering...")
                        TextToSpeech(answer)
                        break
                    elif "realtime" in queries:
                        SetAsssistantStatus("Searching...")
                        query_final = queries.replace("realtime", "")
                        answer = RealtimeSearchEngine(query_final)
                        ShowTextToScreen(f"{Assistantname}: {answer}")
                        SetAsssistantStatus("Answering...")
                        TextToSpeech(answer)
                        break
                    elif "exit" in queries:
                        answer = "Okay, goodbye!"
                        ShowTextToScreen(f"{Assistantname}: {answer}")
                        TextToSpeech(answer)
                        exit_jarvis()
                        return
            
            # Show notification with response
            if background_mode:
                background_mode.show_notification(
                    "Jarvis",
                    "Command completed!"
                )
        
    except Exception as e:
        print(f"Error processing command: {e}")
        if background_mode:
            background_mode.show_notification(
                "Jarvis Error",
                "Failed to process command"
            )
    
    finally:
        is_listening = False
        SetMicrophoneStatus("False")
        SetAsssistantStatus("Available...")
        print("="*60)


def exit_jarvis():
    """Called when exiting Jarvis"""
    print("\n👋 Shutting down Jarvis...")
    
    # Cleanup
    if background_mode:
        background_mode.cleanup()
    
    # Exit
    os._exit(0)


def gui_thread():
    """Run GUI in separate thread"""
    try:
        GraphicalUserInterface()
    except Exception as e:
        print(f"GUI Error: {e}")


def main():
    """Main entry point for background mode"""
    global background_mode
    
    print("\n" + "="*60)
    print("🤖 JARVIS AI ASSISTANT - BACKGROUND MODE")
    print("="*60)
    print(f"User: {Username}")
    print(f"Assistant: {Assistantname}")
    print("="*60)
    
    # Initialize
    SetMicrophoneStatus("False")
    SetAsssistantStatus("Available...")
    ShowTextToScreen(f"{Assistantname}: Running in background mode...")
    
    # Create background mode instance
    background_mode = BackgroundMode(
        on_activate_callback=activate_jarvis,
        on_exit_callback=exit_jarvis
    )
    
    # Setup hotkey (Ctrl+Shift+J)
    hotkey = "ctrl+shift+j"
    if background_mode.setup_hotkey(hotkey):
        print(f"✅ Hotkey: {hotkey}")
    else:
        print(f"❌ Failed to setup hotkey")
    
    # Setup system tray
    if background_mode.setup_system_tray(f"{Assistantname} AI"):
        print(f"✅ System tray icon created")
    else:
        print(f"⚠️  System tray not available (PyQt5 required)")
    
    print("\n" + "="*60)
    print("JARVIS IS NOW RUNNING IN BACKGROUND")
    print("="*60)
    print(f"Press {hotkey} to activate Jarvis")
    print("Right-click tray icon for options")
    print("="*60 + "\n")
    
    # Start GUI in separate thread
    gui_thread_obj = threading.Thread(target=gui_thread, daemon=True)
    gui_thread_obj.start()
    
    # Start floating input window
    print("🔵 Starting floating text input window...")
    floating_thread = threading.Thread(target=start_floating_input, daemon=True)
    floating_thread.start()
    
    # Start text input monitor
    print("🔵 Starting text input monitor...")
    text_monitor_thread = threading.Thread(target=monitor_text_input, daemon=True)
    text_monitor_thread.start()
    
    # Run background mode (blocking)
    try:
        background_mode.run()
    except KeyboardInterrupt:
        print("\n👋 Exiting...")
        exit_jarvis()


if __name__ == "__main__":
    main()
