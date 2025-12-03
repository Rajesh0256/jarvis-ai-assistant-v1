"""
Login Page GUI for Jarvis AI Assistant
"""
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QLineEdit, QMessageBox, QFrame)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
import os
import sys

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Backend.Authentication import AuthenticationSystem


class LoginPage(QWidget):
    login_successful = pyqtSignal(str)  # Signal emitted when login succeeds
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.auth_system = AuthenticationSystem()
        self.init_ui()
    
    def init_ui(self):
        self.setStyleSheet("background-color: #1a1a1a;")
        
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        
        # Login container
        container = QFrame()
        container.setStyleSheet("""
            QFrame {
                background-color: #2d2d2d;
                border-radius: 15px;
                padding: 20px;
            }
        """)
        container.setFixedWidth(400)
        
        layout = QVBoxLayout(container)
        layout.setSpacing(20)
        layout.setContentsMargins(40, 40, 40, 40)
        
        # Title
        title = QLabel("JARVIS AI")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #00d4ff; font-size: 32px; font-weight: bold; border: none;")
        layout.addWidget(title)
        
        subtitle = QLabel("Authentication Required")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: #888; font-size: 14px; border: none;")
        layout.addWidget(subtitle)
        
        layout.addSpacing(20)
        
        # Username field
        username_label = QLabel("Username")
        username_label.setStyleSheet("color: white; font-size: 14px; border: none;")
        layout.addWidget(username_label)
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        self.username_input.setStyleSheet(self.get_input_style())
        self.username_input.setFixedHeight(40)
        layout.addWidget(self.username_input)
        
        # Password field
        password_label = QLabel("Password")
        password_label.setStyleSheet("color: white; font-size: 14px; border: none;")
        layout.addWidget(password_label)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(self.get_input_style())
        self.password_input.setFixedHeight(40)
        self.password_input.returnPressed.connect(self.handle_login)
        layout.addWidget(self.password_input)
        
        layout.addSpacing(10)
        
        # Login button
        self.login_btn = QPushButton("LOGIN")
        self.login_btn.setStyleSheet(self.get_button_style())
        self.login_btn.setFixedHeight(45)
        self.login_btn.clicked.connect(self.handle_login)
        layout.addWidget(self.login_btn)
        
        # Register button
        self.register_btn = QPushButton("CREATE NEW ACCOUNT")
        self.register_btn.setStyleSheet(self.get_secondary_button_style())
        self.register_btn.setFixedHeight(40)
        self.register_btn.clicked.connect(self.show_register_page)
        layout.addWidget(self.register_btn)
        
        # Status label
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #ff4444; font-size: 12px; border: none;")
        layout.addWidget(self.status_label)
        
        main_layout.addWidget(container)
        self.setLayout(main_layout)
    
    def get_input_style(self):
        return """
            QLineEdit {
                background-color: #1a1a1a;
                border: 2px solid #444;
                border-radius: 8px;
                padding: 10px;
                color: white;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #00d4ff;
            }
        """
    
    def get_button_style(self):
        return """
            QPushButton {
                background-color: #00d4ff;
                color: black;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00b8e6;
            }
            QPushButton:pressed {
                background-color: #0099cc;
            }
        """
    
    def get_secondary_button_style(self):
        return """
            QPushButton {
                background-color: transparent;
                color: #00d4ff;
                border: 2px solid #00d4ff;
                border-radius: 8px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #00d4ff;
                color: black;
            }
        """
    
    def handle_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text()
        
        if not username or not password:
            self.status_label.setText("Please fill in all fields")
            return
        
        success, message = self.auth_system.login_user(username, password)
        
        if success:
            self.status_label.setStyleSheet("color: #44ff44; font-size: 12px; border: none;")
            self.status_label.setText(message)
            self.login_successful.emit(username)
        else:
            self.status_label.setStyleSheet("color: #ff4444; font-size: 12px; border: none;")
            self.status_label.setText(message)
    
    def show_register_page(self):
        self.register_window = RegisterPage(self.auth_system)
        self.register_window.registration_successful.connect(self.on_registration_success)
        self.register_window.show()
    
    def on_registration_success(self, username):
        self.username_input.setText(username)
        self.password_input.clear()
        self.password_input.setFocus()
        self.status_label.setStyleSheet("color: #44ff44; font-size: 12px; border: none;")
        self.status_label.setText("Registration successful! Please login.")


class RegisterPage(QWidget):
    registration_successful = pyqtSignal(str)
    
    def __init__(self, auth_system, parent=None):
        super().__init__(parent)
        self.auth_system = auth_system
        self.setWindowTitle("Register - Jarvis AI")
        self.setFixedSize(450, 600)
        self.init_ui()
    
    def init_ui(self):
        self.setStyleSheet("background-color: #1a1a1a;")
        
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        
        container = QFrame()
        container.setStyleSheet("""
            QFrame {
                background-color: #2d2d2d;
                border-radius: 15px;
                padding: 20px;
            }
        """)
        
        layout = QVBoxLayout(container)
        layout.setSpacing(15)
        layout.setContentsMargins(40, 40, 40, 40)
        
        # Title
        title = QLabel("Create Account")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #00d4ff; font-size: 28px; font-weight: bold; border: none;")
        layout.addWidget(title)
        
        layout.addSpacing(20)
        
        # Username
        username_label = QLabel("Username")
        username_label.setStyleSheet("color: white; font-size: 14px; border: none;")
        layout.addWidget(username_label)
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Choose a username")
        self.username_input.setStyleSheet(self.get_input_style())
        self.username_input.setFixedHeight(40)
        layout.addWidget(self.username_input)
        
        # Email (optional)
        email_label = QLabel("Email (Optional)")
        email_label.setStyleSheet("color: white; font-size: 14px; border: none;")
        layout.addWidget(email_label)
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("your.email@example.com")
        self.email_input.setStyleSheet(self.get_input_style())
        self.email_input.setFixedHeight(40)
        layout.addWidget(self.email_input)
        
        # Password
        password_label = QLabel("Password")
        password_label.setStyleSheet("color: white; font-size: 14px; border: none;")
        layout.addWidget(password_label)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("At least 6 characters")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(self.get_input_style())
        self.password_input.setFixedHeight(40)
        layout.addWidget(self.password_input)
        
        # Confirm Password
        confirm_label = QLabel("Confirm Password")
        confirm_label.setStyleSheet("color: white; font-size: 14px; border: none;")
        layout.addWidget(confirm_label)
        
        self.confirm_input = QLineEdit()
        self.confirm_input.setPlaceholderText("Re-enter password")
        self.confirm_input.setEchoMode(QLineEdit.Password)
        self.confirm_input.setStyleSheet(self.get_input_style())
        self.confirm_input.setFixedHeight(40)
        layout.addWidget(self.confirm_input)
        
        layout.addSpacing(10)
        
        # Register button
        register_btn = QPushButton("CREATE ACCOUNT")
        register_btn.setStyleSheet(self.get_button_style())
        register_btn.setFixedHeight(45)
        register_btn.clicked.connect(self.handle_register)
        layout.addWidget(register_btn)
        
        # Status label
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #ff4444; font-size: 12px; border: none;")
        self.status_label.setWordWrap(True)
        layout.addWidget(self.status_label)
        
        main_layout.addWidget(container)
        self.setLayout(main_layout)
    
    def get_input_style(self):
        return """
            QLineEdit {
                background-color: #1a1a1a;
                border: 2px solid #444;
                border-radius: 8px;
                padding: 10px;
                color: white;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #00d4ff;
            }
        """
    
    def get_button_style(self):
        return """
            QPushButton {
                background-color: #00d4ff;
                color: black;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00b8e6;
            }
        """
    
    def handle_register(self):
        username = self.username_input.text().strip()
        email = self.email_input.text().strip()
        password = self.password_input.text()
        confirm = self.confirm_input.text()
        
        if not username or not password:
            self.status_label.setText("Username and password are required")
            return
        
        if password != confirm:
            self.status_label.setText("Passwords do not match")
            return
        
        success, message = self.auth_system.register_user(username, password, email)
        
        if success:
            self.status_label.setStyleSheet("color: #44ff44; font-size: 12px; border: none;")
            self.status_label.setText(message)
            self.registration_successful.emit(username)
            self.close()
        else:
            self.status_label.setStyleSheet("color: #ff4444; font-size: 12px; border: none;")
            self.status_label.setText(message)
