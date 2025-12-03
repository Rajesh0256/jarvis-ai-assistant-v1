"""
Standalone launcher for floating input window
Run this separately alongside Jarvis
"""

import sys
import os
from PyQt5.QtWidgets import QApplication

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from Frontend.FloatingInput import FloatingInputWindow

if __name__ == "__main__":
    print("=" * 60)
    print("STARTING FLOATING INPUT WINDOW")
    print("=" * 60)
    
    app = QApplication(sys.argv)
    window = FloatingInputWindow()
    window.show()
    
    print("✅ Floating input window is now running!")
    print("   Type commands and press Enter")
    print("   Close window or press Ctrl+C to exit")
    print("=" * 60)
    
    sys.exit(app.exec_())
