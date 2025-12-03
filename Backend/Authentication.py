"""
Authentication module for Jarvis AI Assistant
Handles user registration, login, and password management
"""
import json
import hashlib
import os
from datetime import datetime


class AuthenticationSystem:
    def __init__(self, users_file='Data/users.json'):
        self.users_file = users_file
        self.ensure_users_file()
    
    def ensure_users_file(self):
        """Create users file if it doesn't exist"""
        os.makedirs(os.path.dirname(self.users_file), exist_ok=True)
        if not os.path.exists(self.users_file):
            with open(self.users_file, 'w', encoding='utf-8') as f:
                json.dump({}, f)
    
    def hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, username, password, email=''):
        """Register a new user"""
        with open(self.users_file, 'r', encoding='utf-8') as f:
            users = json.load(f)
        
        if username in users:
            return False, "Username already exists"
        
        if len(password) < 6:
            return False, "Password must be at least 6 characters"
        
        users[username] = {
            'password': self.hash_password(password),
            'email': email,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'last_login': None
        }
        
        with open(self.users_file, 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=4)
        
        return True, "Registration successful"
    
    def login_user(self, username, password):
        """Authenticate user login"""
        try:
            with open(self.users_file, 'r', encoding='utf-8') as f:
                users = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return False, "No users registered"
        
        if username not in users:
            return False, "Invalid username or password"
        
        if users[username]['password'] != self.hash_password(password):
            return False, "Invalid username or password"
        
        # Update last login
        users[username]['last_login'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.users_file, 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=4)
        
        return True, "Login successful"
    
    def change_password(self, username, old_password, new_password):
        """Change user password"""
        with open(self.users_file, 'r', encoding='utf-8') as f:
            users = json.load(f)
        
        if username not in users:
            return False, "User not found"
        
        if users[username]['password'] != self.hash_password(old_password):
            return False, "Incorrect old password"
        
        if len(new_password) < 6:
            return False, "New password must be at least 6 characters"
        
        users[username]['password'] = self.hash_password(new_password)
        
        with open(self.users_file, 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=4)
        
        return True, "Password changed successfully"
    
    def user_exists(self, username):
        """Check if user exists"""
        try:
            with open(self.users_file, 'r', encoding='utf-8') as f:
                users = json.load(f)
            return username in users
        except (FileNotFoundError, json.JSONDecodeError):
            return False
