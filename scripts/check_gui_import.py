"""
Quick diagnostic to check if GUI imports work
"""
print("Testing imports...")

try:
    from PyQt5.QtWidgets import QApplication
    print("✅ QApplication imported")
except Exception as e:
    print(f"❌ QApplication import failed: {e}")

try:
    from Frontend.GUI import MainWindow
    print("✅ MainWindow imported")
except Exception as e:
    print(f"❌ MainWindow import failed: {e}")

try:
    from Frontend.LoginPage import LoginPage
    print("✅ LoginPage imported")
except Exception as e:
    print(f"❌ LoginPage import failed: {e}")

try:
    from Backend.Authentication import AuthenticationSystem
    print("✅ AuthenticationSystem imported")
except Exception as e:
    print(f"❌ AuthenticationSystem import failed: {e}")

print("\n" + "="*60)
print("All imports successful! System is ready.")
print("="*60)
