# 🔐 Jarvis Authentication System Guide

## Overview
Jarvis now includes a secure authentication system with a modern login page. Users must authenticate before accessing the AI assistant.

## Features
- ✅ User registration with username and password
- ✅ Secure password hashing (SHA-256)
- ✅ Modern, dark-themed login interface
- ✅ Email field (optional)
- ✅ Password validation (minimum 6 characters)
- ✅ User session tracking (last login time)
- ✅ Easy account creation from login page

## How to Use

### First Time Setup
1. Run Jarvis: `python Main.py`
2. Click **"CREATE NEW ACCOUNT"** button
3. Fill in:
   - Username (required)
   - Email (optional)
   - Password (minimum 6 characters)
   - Confirm Password
4. Click **"CREATE ACCOUNT"**
5. You'll be redirected back to login page
6. Enter your credentials and click **"LOGIN"**

### Regular Login
1. Run Jarvis: `python Main.py`
2. Enter your username and password
3. Press Enter or click **"LOGIN"**
4. Jarvis will start after successful authentication

## Testing Authentication Only
To test the login system without starting full Jarvis:
```bash
python test_authentication.py
```

## File Structure
```
├── Backend/
│   └── Authentication.py       # Authentication logic
├── Frontend/
│   └── LoginPage.py           # Login/Register GUI
├── Data/
│   └── users.json             # User database (auto-created)
└── Main.py                    # Updated with auth integration
```

## Security Features
- **Password Hashing**: Passwords are hashed using SHA-256 (never stored in plain text)
- **Input Validation**: Username and password requirements enforced
- **Secure Storage**: User data stored in JSON with hashed passwords
- **Session Tracking**: Last login timestamp recorded

## User Data Storage
User information is stored in `Data/users.json`:
```json
{
    "username": {
        "password": "hashed_password_here",
        "email": "user@example.com",
        "created_at": "2024-12-01 10:30:00",
        "last_login": "2024-12-01 15:45:00"
    }
}
```

## Customization

### Change Password Requirements
Edit `Backend/Authentication.py`:
```python
if len(password) < 6:  # Change minimum length here
    return False, "Password must be at least 6 characters"
```

### Modify UI Colors
Edit `Frontend/LoginPage.py` color codes:
- Primary color: `#00d4ff` (cyan blue)
- Background: `#1a1a1a` (dark)
- Container: `#2d2d2d` (lighter dark)

### Disable Authentication (Optional)
To run Jarvis without login, modify `Main.py`:
```python
if __name__ == "__main__":
    # Comment out authentication
    # start_jarvis_with_auth()
    
    # Use original startup
    InitialExecution()
    thread1 = threading.Thread(target=FirstThread, daemon=True)
    thread1.start()
    SecondThread()
```

## Troubleshooting

### "No users registered" error
- The `Data/users.json` file is missing or corrupted
- Solution: Delete the file and create a new account

### Can't remember password
- Currently no password recovery (future feature)
- Solution: Manually edit `Data/users.json` to remove your user and re-register

### Login page doesn't appear
- Check if PyQt5 is installed: `pip install PyQt5`
- Verify `Frontend/LoginPage.py` exists

## Future Enhancements
- [ ] Password recovery via email
- [ ] Multi-factor authentication
- [ ] Biometric authentication integration
- [ ] User profile management
- [ ] Password strength indicator
- [ ] Remember me functionality
- [ ] Session timeout

## Notes
- First user created becomes the default user
- Multiple users can be registered
- Each user gets their own login timestamp
- User data persists between sessions
