"""
Floating Text Input Window for Jarvis
Small, always-on-top window for text commands
"""

from PyQt5.QtWidgets import (QWidget, QLineEdit, QPushButton, QVBoxLayout, 
                              QHBoxLayout, QLabel, QApplication)
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont, QIcon
import sys
import os

# Get paths
current_dir = os.getcwd()
TempDirPath = rf"{current_dir}\Frontend\Files"


def TempDirectoryPath(filename):
    """Get path to temp file"""
    return os.path.join(TempDirPath, filename)


def SetMicrophoneStatus(status):
    """Set microphone status"""
    with open(TempDirectoryPath('Mic.data'), 'w', encoding='utf-8') as file:
        file.write(status)


class FloatingInputWindow(QWidget):
    """Small floating window for text input"""
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.dragging = False
        self.offset = QPoint()
        
    def initUI(self):
        """Initialize the UI"""
        # Window settings
        self.setWindowTitle("Jarvis Input")
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint |  # Always on top
            Qt.FramelessWindowHint |    # No title bar
            Qt.Tool                      # Tool window (doesn't show in taskbar)
        )
        
        # Set size
        self.setFixedSize(400, 80)
        
        # Create layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(5)
        
        # Title bar (for dragging)
        title_layout = QHBoxLayout()
        title_label = QLabel("🎤 Jarvis")
        title_label.setStyleSheet("""
            color: white;
            font-size: 12px;
            font-weight: bold;
        """)
        
        # Minimize button
        minimize_btn = QPushButton("−")
        minimize_btn.setFixedSize(20, 20)
        minimize_btn.setStyleSheet("""
            QPushButton {
                background-color: #FFA500;
                color: white;
                border: none;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #FF8C00;
            }
        """)
        minimize_btn.clicked.connect(self.hide)
        
        # Close button
        close_btn = QPushButton("×")
        close_btn.setFixedSize(20, 20)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF4444;
                color: white;
                border: none;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #CC0000;
            }
        """)
        close_btn.clicked.connect(self.close)
        
        title_layout.addWidget(title_label)
        title_layout.addStretch()
        title_layout.addWidget(minimize_btn)
        title_layout.addWidget(close_btn)
        
        # Input section
        input_layout = QHBoxLayout()
        
        # Text input
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Type command here...")
        self.text_input.setStyleSheet("""
            QLineEdit {
                background-color: #2a2a2a;
                color: white;
                border: 2px solid #0096FF;
                border-radius: 5px;
                padding: 8px;
                font-size: 13px;
            }
            QLineEdit:focus {
                border: 2px solid #00BFFF;
            }
        """)
        self.text_input.returnPressed.connect(self.sendCommand)
        
        # Send button
        self.send_btn = QPushButton("Send")
        self.send_btn.setFixedWidth(60)
        self.send_btn.setStyleSheet("""
            QPushButton {
                background-color: #0096FF;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00BFFF;
            }
            QPushButton:pressed {
                background-color: #0080DD;
            }
        """)
        self.send_btn.clicked.connect(self.sendCommand)
        
        input_layout.addWidget(self.text_input)
        input_layout.addWidget(self.send_btn)
        
        # Add to main layout
        main_layout.addLayout(title_layout)
        main_layout.addLayout(input_layout)
        
        self.setLayout(main_layout)
        
        # Style the window
        self.setStyleSheet("""
            QWidget {
                background-color: #1a1a1a;
                border: 2px solid #0096FF;
                border-radius: 10px;
            }
        """)
        
        # Position at bottom right of screen
        self.positionWindow()
        
    def positionWindow(self):
        """Position window at bottom right of screen"""
        screen = QApplication.desktop().screenGeometry()
        x = screen.width() - self.width() - 20
        y = screen.height() - self.height() - 60
        self.move(x, y)
        
    def sendCommand(self):
        """Send command to Jarvis"""
        command = self.text_input.text().strip()
        if command:
            print(f"🔵 Floating Input: Command received: '{command}'")
            
            # Write to text input file
            try:
                with open(TempDirectoryPath('TextInput.data'), 'w', encoding='utf-8') as file:
                    file.write(command)
                print(f"🔵 Floating Input: Written to TextInput.data")
                
                # Set status to Text
                SetMicrophoneStatus("Text")
                print(f"🔵 Floating Input: Status set to 'Text'")
                
                # Clear input
                self.text_input.clear()
                
                # Show feedback
                self.text_input.setPlaceholderText("Command sent! Type next...")
                
            except Exception as e:
                print(f"❌ Floating Input Error: {e}")
                self.text_input.setPlaceholderText(f"Error: {e}")
    
    def mousePressEvent(self, event):
        """Handle mouse press for dragging"""
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()
    
    def mouseMoveEvent(self, event):
        """Handle mouse move for dragging"""
        if self.dragging:
            self.move(self.mapToParent(event.pos() - self.offset))
    
    def mouseReleaseEvent(self, event):
        """Handle mouse release"""
        if event.button() == Qt.LeftButton:
            self.dragging = False


def show_floating_input():
    """Show the floating input window"""
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    
    window = FloatingInputWindow()
    window.show()
    
    return window


# Test
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FloatingInputWindow()
    window.show()
    sys.exit(app.exec_())
