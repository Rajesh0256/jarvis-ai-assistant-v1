import pyautogui
import time
import os

class ApplicationLauncher:
    def __init__(self):
        """Initialize the Application Launcher"""
        pass
    
    def open_application(self, app_name):
        """
        Open an application using Windows search bar
        Args:
            app_name: Name of the application to open
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Press Windows key to open start menu/search
            pyautogui.press('win')
            time.sleep(0.5)
            
            # Type the application name
            pyautogui.write(app_name, interval=0.05)
            time.sleep(0.8)
            
            # Press Enter to open the first result
            pyautogui.press('enter')
            
            return True
            
        except Exception as e:
            print(f"Error opening application: {e}")
            return False
    
    def open_application_with_path(self, app_path):
        """
        Open an application directly using its path
        Args:
            app_path: Full path to the application executable
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            os.startfile(app_path)
            return True
        except Exception as e:
            print(f"Error opening application from path: {e}")
            return False
