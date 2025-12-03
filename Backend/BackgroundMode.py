"""Background Mode for Jarvis - System Tray Integration"""
import sys
import os
import keyboard
import threading
from time import sleep

try:
    from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
    from PyQt5.QtGui import QIcon
    from PyQt5.QtCore import QTimer
    PYQT5_AVAILABLE = True
except ImportError:
    PYQT5_AVAILABLE = False
    print("PyQt5 not available for system tray. Background mode will use keyboard hotkey only.")


class BackgroundMode:
    """Manages Jarvis running in background with system tray icon"""
    
    def __init__(self, on_activate_callback=None, on_exit_callback=None):
        """
        Initialize background mode
        
        Args:
            on_activate_callback: Function to call when Jarvis is activated
            on_exit_callback: Function to call when exiting
        """
        self.on_activate = on_activate_callback
        self.on_exit = on_exit_callback
        self.is_running = True
        self.hotkey = "ctrl+shift+j"  # Default hotkey
        self.tray_icon = None
        self.app = None
        
    def setup_hotkey(self, hotkey="ctrl+shift+j"):
        """Setup global hotkey to activate Jarvis"""
        self.hotkey = hotkey
        try:
            keyboard.add_hotkey(hotkey, self._on_hotkey_pressed)
            print(f"✅ Hotkey registered: {hotkey}")
            return True
        except Exception as e:
            print(f"❌ Failed to register hotkey: {e}")
            return False
    
    def _on_hotkey_pressed(self):
        """Called when hotkey is pressed"""
        print(f"\n🎤 Hotkey pressed: {self.hotkey}")
        if self.on_activate:
            try:
                self.on_activate()
            except Exception as e:
                print(f"Error in activation callback: {e}")
    
    def setup_system_tray(self, app_name="Jarvis AI", icon_path=None):
        """Setup system tray icon"""
        if not PYQT5_AVAILABLE:
            print("PyQt5 not available. System tray disabled.")
            return False
        
        try:
            # Create QApplication if not exists
            if not QApplication.instance():
                self.app = QApplication(sys.argv)
            else:
                self.app = QApplication.instance()
            
            # Create system tray icon
            self.tray_icon = QSystemTrayIcon()
            
            # Set icon (use default if no icon provided)
            if icon_path and os.path.exists(icon_path):
                icon = QIcon(icon_path)
            else:
                # Use default system icon
                icon = self.app.style().standardIcon(
                    self.app.style().SP_ComputerIcon
                )
            
            self.tray_icon.setIcon(icon)
            self.tray_icon.setToolTip(f"{app_name} - Running in background")
            
            # Create context menu
            menu = QMenu()
            
            # Show/Activate action
            show_action = QAction("Activate Jarvis", menu)
            show_action.triggered.connect(self._on_show_clicked)
            menu.addAction(show_action)
            
            # Separator
            menu.addSeparator()
            
            # Hotkey info
            hotkey_action = QAction(f"Hotkey: {self.hotkey}", menu)
            hotkey_action.setEnabled(False)
            menu.addAction(hotkey_action)
            
            # Separator
            menu.addSeparator()
            
            # Exit action
            exit_action = QAction("Exit", menu)
            exit_action.triggered.connect(self._on_exit_clicked)
            menu.addAction(exit_action)
            
            self.tray_icon.setContextMenu(menu)
            
            # Show notification on double-click
            self.tray_icon.activated.connect(self._on_tray_activated)
            
            # Show the tray icon
            self.tray_icon.show()
            
            # Show notification
            self.show_notification(
                f"{app_name} Running",
                f"Press {self.hotkey} to activate\nRight-click tray icon for options"
            )
            
            print(f"✅ System tray icon created")
            return True
            
        except Exception as e:
            print(f"❌ Failed to create system tray: {e}")
            return False
    
    def _on_tray_activated(self, reason):
        """Called when tray icon is clicked"""
        if reason == QSystemTrayIcon.DoubleClick:
            self._on_show_clicked()
    
    def _on_show_clicked(self):
        """Called when 'Show' is clicked in tray menu"""
        print("\n🎤 Activating Jarvis from tray...")
        if self.on_activate:
            try:
                self.on_activate()
            except Exception as e:
                print(f"Error in activation callback: {e}")
    
    def _on_exit_clicked(self):
        """Called when 'Exit' is clicked in tray menu"""
        print("\n👋 Exiting Jarvis...")
        self.is_running = False
        
        if self.on_exit:
            try:
                self.on_exit()
            except Exception as e:
                print(f"Error in exit callback: {e}")
        
        # Cleanup
        if self.tray_icon:
            self.tray_icon.hide()
        
        # Exit application
        if self.app:
            self.app.quit()
        
        sys.exit(0)
    
    def show_notification(self, title, message, duration=3000):
        """Show system tray notification"""
        if self.tray_icon and PYQT5_AVAILABLE:
            try:
                self.tray_icon.showMessage(
                    title,
                    message,
                    QSystemTrayIcon.Information,
                    duration
                )
            except Exception as e:
                print(f"Failed to show notification: {e}")
    
    def run(self):
        """Run the background mode (blocking)"""
        if self.app and PYQT5_AVAILABLE:
            # Run Qt event loop
            sys.exit(self.app.exec_())
        else:
            # Fallback: just keep running
            print("Running in background mode (hotkey only)...")
            print(f"Press {self.hotkey} to activate Jarvis")
            print("Press Ctrl+C to exit")
            
            try:
                while self.is_running:
                    sleep(1)
            except KeyboardInterrupt:
                print("\n👋 Exiting...")
                if self.on_exit:
                    self.on_exit()
    
    def cleanup(self):
        """Cleanup resources"""
        try:
            keyboard.unhook_all_hotkeys()
        except:
            pass
        
        if self.tray_icon:
            self.tray_icon.hide()


# Standalone test
if __name__ == "__main__":
    def test_activate():
        print("🎤 Jarvis activated!")
    
    def test_exit():
        print("👋 Goodbye!")
    
    bg = BackgroundMode(
        on_activate_callback=test_activate,
        on_exit_callback=test_exit
    )
    
    bg.setup_hotkey("ctrl+shift+j")
    bg.setup_system_tray("Jarvis AI Test")
    
    print("\n" + "="*60)
    print("JARVIS BACKGROUND MODE TEST")
    print("="*60)
    print(f"Hotkey: {bg.hotkey}")
    print("System tray icon should be visible")
    print("Press Ctrl+C to exit")
    print("="*60 + "\n")
    
    bg.run()
