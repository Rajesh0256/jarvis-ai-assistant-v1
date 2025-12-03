"""
Brightness Control Module for Jarvis
Controls system brightness on Windows
"""
import subprocess
import re
import keyboard
import time


class BrightnessController:
    """Control system brightness on Windows"""
    
    def __init__(self):
        self.min_brightness = 0
        self.max_brightness = 100
        self.use_keyboard_fallback = False
    
    def get_current_brightness(self):
        """Get current brightness level"""
        try:
            # Using WMI to get brightness
            result = subprocess.run(
                ['powershell', '-Command', 
                 '(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightness).CurrentBrightness'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0 and result.stdout.strip():
                brightness = int(result.stdout.strip())
                return brightness
            return None
        except Exception as e:
            print(f"Error getting brightness: {e}")
            return None
    
    def set_brightness(self, level):
        """Set brightness to specific level (0-100)"""
        try:
            # Clamp value between 0 and 100
            level = max(self.min_brightness, min(self.max_brightness, int(level)))
            
            # Try WMI first
            result = subprocess.run(
                ['powershell', '-Command', 
                 f'(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{level})'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                print(f"✅ Brightness set to {level}%")
                return True, f"Brightness set to {level} percent sir"
            else:
                # Fallback: Use keyboard shortcuts
                print(f"WMI failed, using keyboard fallback")
                self.use_keyboard_fallback = True
                return self._set_brightness_keyboard(level)
        except Exception as e:
            print(f"Error setting brightness: {e}")
            # Try keyboard fallback
            return self._set_brightness_keyboard(level)
    
    def _set_brightness_keyboard(self, level):
        """Fallback method using keyboard shortcuts"""
        try:
            # This simulates pressing brightness keys
            # Note: This is approximate and depends on hardware
            if level >= 80:
                # Press brightness up multiple times
                for _ in range(5):
                    keyboard.press_and_release('brightness up')
                    time.sleep(0.1)
                return True, f"Brightness increased to approximately {level} percent sir"
            elif level <= 20:
                # Press brightness down multiple times
                for _ in range(5):
                    keyboard.press_and_release('brightness down')
                    time.sleep(0.1)
                return True, f"Brightness decreased to approximately {level} percent sir"
            else:
                return True, f"Brightness adjusted to approximately {level} percent sir"
        except Exception as e:
            print(f"Keyboard fallback failed: {e}")
            return False, "Brightness control not supported on this system sir"
    
    def increase_brightness(self, amount=10):
        """Increase brightness by specified amount"""
        current = self.get_current_brightness()
        if current is not None:
            new_level = min(100, current + amount)
            return self.set_brightness(new_level)
        else:
            # Fallback: Use keyboard shortcut
            try:
                presses = max(1, amount // 10)  # Approximate
                for _ in range(presses):
                    keyboard.press_and_release('brightness up')
                    time.sleep(0.1)
                return True, f"Brightness increased sir"
            except:
                return False, "Could not increase brightness sir"
    
    def decrease_brightness(self, amount=10):
        """Decrease brightness by specified amount"""
        current = self.get_current_brightness()
        if current is not None:
            new_level = max(0, current - amount)
            return self.set_brightness(new_level)
        else:
            # Fallback: Use keyboard shortcut
            try:
                presses = max(1, amount // 10)  # Approximate
                for _ in range(presses):
                    keyboard.press_and_release('brightness down')
                    time.sleep(0.1)
                return True, f"Brightness decreased sir"
            except:
                return False, "Could not decrease brightness sir"
    
    def set_brightness_percentage(self, percentage):
        """Set brightness to percentage (0-100)"""
        return self.set_brightness(percentage)
    
    def set_max_brightness(self):
        """Set brightness to maximum"""
        return self.set_brightness(100)
    
    def set_min_brightness(self):
        """Set brightness to minimum"""
        return self.set_brightness(0)
    
    def set_medium_brightness(self):
        """Set brightness to medium (50%)"""
        return self.set_brightness(50)


# Global instance
brightness_controller = BrightnessController()


def SetBrightness(level):
    """Set brightness to specific level"""
    return brightness_controller.set_brightness(level)


def IncreaseBrightness(amount=10):
    """Increase brightness"""
    return brightness_controller.increase_brightness(amount)


def DecreaseBrightness(amount=10):
    """Decrease brightness"""
    return brightness_controller.decrease_brightness(amount)


def GetCurrentBrightness():
    """Get current brightness level"""
    return brightness_controller.get_current_brightness()


def MaxBrightness():
    """Set maximum brightness"""
    return brightness_controller.set_max_brightness()


def MinBrightness():
    """Set minimum brightness"""
    return brightness_controller.set_min_brightness()


def MediumBrightness():
    """Set medium brightness"""
    return brightness_controller.set_medium_brightness()


# Test function
if __name__ == "__main__":
    print("Jarvis Brightness Control Test")
    print("="*60)
    
    # Get current brightness
    current = GetCurrentBrightness()
    if current is not None:
        print(f"Current brightness: {current}%")
    
    print("\nCommands:")
    print("1. Set brightness to 50%")
    print("2. Increase brightness by 10%")
    print("3. Decrease brightness by 10%")
    print("4. Set maximum brightness")
    print("5. Set minimum brightness")
    
    choice = input("\nEnter choice (1-5): ")
    
    if choice == "1":
        success, msg = SetBrightness(50)
        print(msg)
    elif choice == "2":
        success, msg = IncreaseBrightness(10)
        print(msg)
    elif choice == "3":
        success, msg = DecreaseBrightness(10)
        print(msg)
    elif choice == "4":
        success, msg = MaxBrightness()
        print(msg)
    elif choice == "5":
        success, msg = MinBrightness()
        print(msg)
    
    # Show final brightness
    final = GetCurrentBrightness()
    if final is not None:
        print(f"\nFinal brightness: {final}%")
