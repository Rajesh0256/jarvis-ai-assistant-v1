from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QStackedWidget, QWidget, QLineEdit, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QLabel, QSizePolicy, QSystemTrayIcon, QMenu, QAction)
from PyQt5.QtGui import QIcon, QPainter, QMovie, QColor, QTextCharFormat, QFont, QPixmap, QTextBlockFormat
from PyQt5.QtCore import Qt, QSize, QTimer
from dotenv import dotenv_values
import sys
import os

# Load environment variables
env_vars = dotenv_values(".env")
Assistantname = env_vars.get("Assistantname")
old_chat_message = ""
# Directory paths
current_dir = os.getcwd()
TempDirPath = rf"{current_dir}\Frontend\Files"
GraphicsDirPath = rf"{current_dir}\Frontend\Graphics"

def AnswerModifier(Answer):
    lines = Answer.split('\n')
    non_empty_lines = [line.strip() for line in lines if line.strip()]
    modified_answer = '\n'.join(non_empty_lines)
    return modified_answer


def QueryModifier(Query):
    new_query = Query.lower().strip()
    query_words  = new_query.split()
    question_words = ['how','what','who','where','when','why','which','whom','can you',"what's", "where's","how's"]

    if any(word + " " in new_query for word in question_words):
        if query_words[-1][-1] in ['.','?','!']:
            new_query = new_query[:-1] + "?"
        else:
            new_query += "?"
    else:
        if query_words[-1][-1] in ['.','?','!']:
            new_query = new_query[:-1] + '.'
        else:
            new_query += '.'

    return new_query.capitalize()


def SetMicrophoneStatus(Command):
    with open(TempDirectoryPath('Mic.data'), 'w', encoding='utf-8') as file:
        file.write(Command)
    

def GetMicrophoneStatus():
    
    with open(TempDirectoryPath('Mic.data'), 'r', encoding='utf-8') as file:
        Status = file.read().strip()
    return Status


def SetAsssistantStatus(Status):
    with open(rf'{TempDirPath}\Status.data','w',encoding='utf-8') as file:
        file.write(Status)


def GetAssistantStatus():
    with open(rf'{TempDirPath}\Status.data', 'r', encoding='utf-8') as file:
        Status = file.read()
    return Status
    

    
# Define placeholders for the missing functions
def MicButtonInitiated():
    SetMicrophoneStatus("False")

def MicButtonClosed():
    SetMicrophoneStatus("True")

def GraphicsDirectoryPath(Filename):
    path = rf'{GraphicsDirPath}\{Filename}'
    return path


def TempDirectoryPath(Filename):
    path = rf'{TempDirPath}\{Filename}'
    return path

def ShowTextToScreen(Text):
    with open (rf'{TempDirPath}\Responses.data','w', encoding='utf-8') as file:
        file.write(Text)

    
class ChatSection(QWidget):
    def __init__(self):
        super(ChatSection, self).__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(-10, 40, 40, 100)
        layout.setSpacing(-100)

        self.chat_text_edit = QTextEdit()
        self.chat_text_edit.setReadOnly(True)
        self.chat_text_edit.setTextInteractionFlags(Qt.NoTextInteraction)
        self.chat_text_edit.setFrameStyle(QFrame.NoFrame)
        layout.addWidget(self.chat_text_edit)

        # Add text input section at the bottom
        input_layout = QHBoxLayout()
        input_layout.setContentsMargins(10, 10, 10, 20)

        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Type your command here...")
        self.text_input.setStyleSheet("""
            QLineEdit {
                background-color: #1a1a1a;
                color: white;
                border: 2px solid #0096FF;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #00BFFF;
            }
        """)
        self.text_input.returnPressed.connect(self.sendTextCommand)

        self.send_button = QPushButton("Send")
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: #0096FF;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00BFFF;
            }
            QPushButton:pressed {
                background-color: #0080DD;
            }
        """)
        self.send_button.clicked.connect(self.sendTextCommand)

        input_layout.addWidget(self.text_input)
        input_layout.addWidget(self.send_button)
        layout.addLayout(input_layout)

        self.setStyleSheet("background-color: black;")
        layout.setSizeConstraint(QVBoxLayout.SetDefaultConstraint)
        layout.setStretch(1, 1)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

        text_color = QColor(Qt.blue)
        text_color_text = QTextCharFormat()
        text_color_text.setForeground(text_color)
        self.chat_text_edit.setCurrentCharFormat(text_color_text)

        self.gif_label = QLabel()
        self.gif_label.setStyleSheet("border: none;")
        movie = QMovie(rf"{GraphicsDirPath}\Jarvis.gif")
        max_gif_size_W = 480
        max_gif_size_H = 270
        movie.setScaledSize(QSize(max_gif_size_W, max_gif_size_H))
        self.gif_label.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.gif_label.setMovie(movie)
        movie.start()
        layout.addWidget(self.gif_label)

        self.label = QLabel("")
        self.label.setStyleSheet("color: white; font-size: 16px; margin-right: 195px; border: none; margin-top: -30px;")
        self.label.setAlignment(Qt.AlignRight)
        layout.addWidget(self.label)

        font = QFont()
        font.setPointSize(13)
        self.chat_text_edit.setFont(font)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.loadMessages)
        self.timer.timeout.connect(self.SpeechRecogText)
        self.timer.start(5)

        self.chat_text_edit.viewport().installEventFilter(self)
        self.setStyleSheet("""
            QScrollBar:vertical {
                border: none;
                background: black;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }

            QScrollBar::handle:vertical {
                background: white;
                min-height: 20px;
            }

            QScrollBar::add-line:vertical {
                background: black;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
                height: 10px;
            }

            QScrollBar::sub-line:vertical {
                background: black;
                subcontrol-position: top;
                subcontrol-origin: margin;
                height: 10px;
            }

            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                border: none;
                background: none;
                color: none;
            }

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }

        """)

    def loadMessages(self):
        global old_chat_message
        try:
            with open(rf'{TempDirPath}\Responses.data', 'r', encoding='utf-8') as file:
                messages = file.read()
            if messages and messages != old_chat_message:
                self.addMessage(message=messages, color='White')
                old_chat_message = messages
        except FileNotFoundError:
            pass

    def SpeechRecogText(self):
        try:
            with open(rf'{TempDirPath}\Status.data', 'r', encoding='utf-8') as file:
                messages = file.read()
            self.label.setText(messages)
        except FileNotFoundError:
            pass

    def load_icon(self, path, width=60, height=60):
        pixmap = QPixmap(path)
        new_pixmap = pixmap.scaled(width, height)
        self.icon_label.setPixmap(new_pixmap)

    def toggle_icon(self, event=None):
        if self.toggled:
            self.load_icon(rf'{GraphicsDirPath}\voice.png', 60, 60)
            MicButtonInitiated()
        else:
            self.load_icon(rf'{GraphicsDirPath}\mic.png', 60, 60)
            MicButtonClosed()
        self.toggled = not self.toggled

    def addMessage(self, message, color):
        cursor = self.chat_text_edit.textCursor()
        format = QTextCharFormat()
        formatm = QTextBlockFormat()
        formatm.setTopMargin(10)
        formatm.setLeftMargin(10)
        format.setForeground(QColor(color))
        cursor.setCharFormat(format)
        cursor.setBlockFormat(formatm)
        cursor.insertText(message + "\n")
        self.chat_text_edit.setTextCursor(cursor)

    def sendTextCommand(self):
        """Handle text input command"""
        print("🔵 GUI (ChatSection): sendTextCommand() called!")
        command = self.text_input.text().strip()
        print(f"🔵 GUI (ChatSection): Command text: '{command}'")
        if command:
            # Write command to text input file
            file_path = TempDirectoryPath('TextInput.data')
            print(f"🔵 GUI (ChatSection): Writing to: {file_path}")
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(command)
            print(f"🔵 GUI (ChatSection): Written command: '{command}'")
            # Clear input field
            self.text_input.clear()
            print("🔵 GUI (ChatSection): Cleared text input field")
            # Set microphone status to trigger command processing
            SetMicrophoneStatus("Text")
            print("🔵 GUI (ChatSection): Set status to 'Text'")
        else:
            print("🔵 GUI (ChatSection): No command entered (empty)")



class InitialScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        desktop = QApplication.desktop()
        screen_width = desktop.screenGeometry().width()
        screen_height = desktop.screenGeometry().height()
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)

        gif_label = QLabel()
        movie = QMovie(GraphicsDirPath + r'\Jarvis.gif')  # Fixed this line
        gif_label.setMovie(movie)
        max_gif_size_H = int(screen_width / 16 * 9)
        movie.setScaledSize(QSize(screen_width, max_gif_size_H))
        gif_label.setAlignment(Qt.AlignCenter)
        movie.start()

        gif_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.icon_label = QLabel()
        pixmap = QPixmap(GraphicsDirPath + r'\Mic_on.png')  # Fixed this line
        new_pixmap = pixmap.scaled(60, 60)
        self.icon_label.setPixmap(new_pixmap)
        self.icon_label.setFixedSize(150, 150)
        self.icon_label.setAlignment(Qt.AlignCenter)
        self.toggled = True
        self.toggle_icon()
        self.icon_label.mousePressEvent = self.toggle_icon

        self.label = QLabel("")
        self.label.setStyleSheet("color: white; font-size: 16px; margin-bottom: 0;")
        content_layout.addWidget(gif_label, alignment=Qt.AlignCenter)
        content_layout.addWidget(self.label, alignment=Qt.AlignCenter)
        content_layout.addWidget(self.icon_label, alignment=Qt.AlignCenter)

        # Add text input section
        input_layout = QHBoxLayout()
        input_layout.setContentsMargins(100, 20, 100, 0)

        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Type your command here...")
        self.text_input.setStyleSheet("""
            QLineEdit {
                background-color: #1a1a1a;
                color: white;
                border: 2px solid #0096FF;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #00BFFF;
            }
        """)
        self.text_input.returnPressed.connect(self.sendTextCommand)

        self.send_button = QPushButton("Send")
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: #0096FF;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00BFFF;
            }
            QPushButton:pressed {
                background-color: #0080DD;
            }
        """)
        self.send_button.clicked.connect(self.sendTextCommand)

        input_layout.addWidget(self.text_input)
        input_layout.addWidget(self.send_button)
        content_layout.addLayout(input_layout)

        content_layout.setContentsMargins(0, 0, 0, 150)
        self.setLayout(content_layout)

        self.setLayout(content_layout)
        self.setFixedHeight(screen_height)
        self.setFixedWidth(screen_width)
        self.setStyleSheet("background-color: black;")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.SpeechRecogText)
        self.timer.start(5)

    def SpeechRecogText(self):
        with open(TempDirPath + r'\Status.data', 'r', encoding='utf-8') as file:  # Fixed this line
            messages = file.read()
            self.label.setText(messages)

    def load_icon(self, path, width=60, height=60):
        pixmap = QPixmap(path)
        new_pixmap = pixmap.scaled(width, height)
        self.icon_label.setPixmap(new_pixmap)

    def toggle_icon(self, event=None):
        if self.toggled:
            self.load_icon(GraphicsDirPath + r'\Mic_on.png', 60, 60)  # Fixed this line
            MicButtonInitiated()  # Ensure this function is defined
        else:
            self.load_icon(GraphicsDirPath + r'\Mic_off.png', 60, 60)  # Fixed this line
            MicButtonClosed()  # Ensure this function is defined
        self.toggled = not self.toggled

    def sendTextCommand(self):
        """Handle text input command"""
        print("🔵 GUI (InitialScreen): sendTextCommand() called!")
        command = self.text_input.text().strip()
        print(f"🔵 GUI (InitialScreen): Command text: '{command}'")
        if command:
            # Write command to text input file
            file_path = TempDirectoryPath('TextInput.data')
            print(f"🔵 GUI (InitialScreen): Writing to: {file_path}")
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(command)
            print(f"🔵 GUI (InitialScreen): Written command: '{command}'")
            # Clear input field
            self.text_input.clear()
            print("🔵 GUI (InitialScreen): Cleared text input field")
            # Set microphone status to trigger command processing
            SetMicrophoneStatus("Text")
            print("🔵 GUI (InitialScreen): Set status to 'Text'")
        else:
            print("🔵 GUI (InitialScreen): No command entered (empty)")


class MessageScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        desktop = QApplication.desktop()
        screen_width = desktop.screenGeometry().width()
        screen_height = desktop.screenGeometry().height()
        layout = QVBoxLayout()
        label = QLabel("")
        layout.addWidget(label)
        chat_section = ChatSection()  # Ensure ChatSection is defined elsewhere
        layout.addWidget(chat_section)
        self.setLayout(layout)
        self.setStyleSheet("background-color: black;")
        self.setFixedHeight(screen_height)
        self.setFixedWidth(screen_width)


class CustomTopBar(QWidget):
    def __init__(self, parent, stacked_widget):
        super().__init__(parent)
        self.stacked_widget = stacked_widget
        self.current_screen = None
        self.initUI()

    def initUI(self):
        self.setFixedHeight(50)
        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignRight)

        home_button = QPushButton()
        home_icon = QIcon(GraphicsDirPath + r'\Home.png')
        home_button.setIcon(home_icon)
        home_button.setText("   Home")
        home_button.setStyleSheet("height:40px; line-height:40px; background-color:white; color: black")
        home_button.clicked.connect(self.showInitialScreen)

        message_button = QPushButton()
        message_icon = QIcon(GraphicsDirPath + r'\Message.png')
        message_button.setIcon(message_icon)
        message_button.setText("   Message")
        message_button.setStyleSheet("height:40px; line-height:40px; background-color:white; color: black")
        message_button.clicked.connect(self.showMessageScreen)

        minimize_button = QPushButton()
        minimize_icon = QIcon(GraphicsDirPath + r'\Minimize.png')
        minimize_button.setIcon(minimize_icon)
        minimize_button.setFlat(True)
        minimize_button.setStyleSheet("background-color:white")
        minimize_button.clicked.connect(self.minimizeWindow)

        self.maximize_button = QPushButton()
        self.maximize_icon = QIcon(GraphicsDirPath + r'\Maximize.png')
        self.restore_icon = QIcon(GraphicsDirPath + r'\Restore.png')
        self.maximize_button.setIcon(self.maximize_icon)
        self.maximize_button.setFlat(True)
        self.maximize_button.setStyleSheet("background-color:white")
        self.maximize_button.clicked.connect(self.maximizeWindow)

        close_button = QPushButton()
        close_icon = QIcon(GraphicsDirPath + r'\Close.png')
        close_button.setIcon(close_icon)
        close_button.setStyleSheet("background-color:white")
        close_button.clicked.connect(self.closeWindow)

        layout.addWidget(home_button)
        layout.addWidget(message_button)
        layout.addWidget(minimize_button)
        layout.addWidget(self.maximize_button)
        layout.addWidget(close_button)

        self.draggable = True
        self.offset = None

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.white)
        super().paintEvent(event)



    def minimizeWindow(self):
        self.parent().showMinimized()

    def maximizeWindow(self):
        if self.parent().isMaximized():
            self.parent().showNormal()
            self.maximize_button.setIcon(self.maximize_icon)
        else:
            self.parent().showMaximized()
            self.maximize_button.setIcon(self.restore_icon)

    def closeWindow(self):
        self.parent().close()

    def showMessageScreen(self):
        self.stacked_widget.setCurrentIndex(1)

    def showInitialScreen(self):
        self.stacked_widget.setCurrentIndex(0)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.initUI()
        self.createSystemTray()

    def initUI(self):
        desktop = QApplication.desktop()
        screen_width = desktop.screenGeometry().width()
        screen_height = desktop.screenGeometry().height()
        stacked_widget = QStackedWidget(self)
        initial_screen = InitialScreen()
        message_screen = MessageScreen()
        stacked_widget.addWidget(initial_screen)
        stacked_widget.addWidget(message_screen)
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setStyleSheet("background-color: black;")
        top_bar = CustomTopBar(self, stacked_widget)
        self.setMenuWidget(top_bar)
        self.setCentralWidget(stacked_widget)
    
    def createSystemTray(self):
        """Create system tray icon for minimizing to tray"""
        # Create system tray icon
        self.tray_icon = QSystemTrayIcon(self)
        
        # Try to load custom icon, fallback to default
        icon_path = os.path.join(GraphicsDirPath, "jarvis_icon.png")
        if os.path.exists(icon_path):
            self.tray_icon.setIcon(QIcon(icon_path))
        else:
            # Create a simple colored icon if custom icon doesn't exist
            pixmap = QPixmap(64, 64)
            pixmap.fill(QColor(0, 150, 255))  # Blue color
            self.tray_icon.setIcon(QIcon(pixmap))
        
        # Create tray menu
        tray_menu = QMenu()
        
        # Show/Hide action
        show_action = QAction("Show Jarvis", self)
        show_action.triggered.connect(self.showNormal)
        tray_menu.addAction(show_action)
        
        hide_action = QAction("Minimize to Tray", self)
        hide_action.triggered.connect(self.hide)
        tray_menu.addAction(hide_action)
        
        tray_menu.addSeparator()
        
        # Status action (non-clickable)
        status_action = QAction("Jarvis is running...", self)
        status_action.setEnabled(False)
        tray_menu.addAction(status_action)
        
        tray_menu.addSeparator()
        
        # Exit action
        exit_action = QAction("Exit Jarvis", self)
        exit_action.triggered.connect(self.closeApplication)
        tray_menu.addAction(exit_action)
        
        self.tray_icon.setContextMenu(tray_menu)
        
        # Double-click to show window
        self.tray_icon.activated.connect(self.onTrayIconActivated)
        
        # Show tray icon
        self.tray_icon.show()
        
        # Show notification
        self.tray_icon.showMessage(
            "Jarvis AI Assistant",
            "Jarvis is running in the background. Double-click to show window.",
            QSystemTrayIcon.Information,
            3000
        )
    
    def onTrayIconActivated(self, reason):
        """Handle tray icon activation (double-click)"""
        if reason == QSystemTrayIcon.DoubleClick:
            if self.isVisible():
                self.hide()
            else:
                self.showNormal()
                self.activateWindow()
    
    def changeEvent(self, event):
        """Override changeEvent to handle minimize to tray"""
        if event.type() == event.WindowStateChange:
            if self.isMinimized():
                # Minimize to tray instead of taskbar
                event.ignore()
                self.hide()
                self.tray_icon.showMessage(
                    "Jarvis AI Assistant",
                    "Jarvis is still running in the background. I'm ready for your commands!",
                    QSystemTrayIcon.Information,
                    2000
                )
                return
        super(MainWindow, self).changeEvent(event)
    
    def closeEvent(self, event):
        """Override close event to minimize to tray instead of closing"""
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
            "Jarvis AI Assistant",
            "Jarvis is still running. Right-click the tray icon to exit.",
            QSystemTrayIcon.Information,
            2000
        )
    
    def closeApplication(self):
        """Actually close the application"""
        self.tray_icon.hide()
        QApplication.quit()

def GraphicalUserInterface(app=None):
    if app is None:
        app = QApplication(sys.argv)
        should_exec = True
    else:
        should_exec = False
    
    window = MainWindow()
    window.show()
    
    if should_exec:
        sys.exit(app.exec_())
# Run the application
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())