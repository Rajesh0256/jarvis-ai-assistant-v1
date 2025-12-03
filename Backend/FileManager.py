import os
import shutil
import subprocess
import platform
from pathlib import Path
from datetime import datetime

# Import winshell only on Windows
try:
    import winshell
    WINSHELL_AVAILABLE = True
except ImportError:
    WINSHELL_AVAILABLE = False


class FileManager:
    """Handles all file and folder operations for Jarvis"""
    
    def __init__(self):
        self.system = platform.system()
        # Common search locations
        self.search_paths = [
            Path.home() / "Desktop",
            Path.home() / "Documents",
            Path.home() / "Downloads",
            Path.home(),
        ]
    
    def open_file_or_folder(self, name):
        """Open a file or folder using the default system application"""
        try:
            # First, try to find the file/folder
            found_path = self.find_file_or_folder(name, return_first=True)
            
            if not found_path:
                return f"I couldn't find {name} in common locations. Please specify the full path."
            
            # Determine if it's a file or folder
            is_folder = os.path.isdir(found_path)
            item_type = "folder" if is_folder else "file"
            
            # Open based on operating system
            if self.system == "Windows":
                os.startfile(found_path)
            elif self.system == "Darwin":  # macOS
                subprocess.run(["open", found_path])
            else:  # Linux
                subprocess.run(["xdg-open", found_path])
            
            # Return personalized message
            return f"{name} {item_type} opening sir"
        
        except Exception as e:
            return f"I encountered an error while opening {name}: {str(e)}"
    
    def delete_file_or_folder(self, name, confirmed=True):
        """Delete a file or folder"""
        try:
            # Find the file/folder first
            found_path = self.find_file_or_folder(name, return_first=True)
            
            if not found_path:
                return f"I couldn't find {name} to delete."
            
            # For voice commands, we auto-confirm but warn the user
            # Perform deletion
            if os.path.isdir(found_path):
                shutil.rmtree(found_path)
                return f"Successfully deleted folder {name} from {os.path.dirname(found_path)}"
            else:
                os.remove(found_path)
                return f"Successfully deleted file {name} from {os.path.dirname(found_path)}"
        
        except PermissionError:
            return f"I don't have permission to delete {name}. Please check file permissions."
        except Exception as e:
            return f"I encountered an error while deleting {name}: {str(e)}"
    
    def create_folder(self, folder_name, location=None):
        """Create a new folder"""
        try:
            if location is None:
                location = Path.home() / "Desktop"
            else:
                location = Path(location)
            
            new_folder_path = location / folder_name
            
            if new_folder_path.exists():
                return f"A folder named {folder_name} already exists at {location}"
            
            os.makedirs(new_folder_path)
            return f"Created new folder {folder_name} at {location}"
        
        except Exception as e:
            return f"I encountered an error while creating folder {folder_name}: {str(e)}"
    
    def find_file_or_folder(self, name, return_first=False):
        """Search for a file or folder in common locations"""
        name_lower = name.lower()
        found_items = []
        
        for search_path in self.search_paths:
            if not search_path.exists():
                continue
            
            try:
                for root, dirs, files in os.walk(search_path):
                    # Check folders
                    for dir_name in dirs:
                        if name_lower in dir_name.lower():
                            full_path = os.path.join(root, dir_name)
                            if return_first:
                                return full_path
                            found_items.append(full_path)
                    
                    # Check files
                    for file_name in files:
                        if name_lower in file_name.lower():
                            full_path = os.path.join(root, file_name)
                            if return_first:
                                return full_path
                            found_items.append(full_path)
                    
                    # Limit depth to avoid too long searches
                    if len(root.split(os.sep)) - len(str(search_path).split(os.sep)) > 3:
                        break
            
            except PermissionError:
                continue
        
        if return_first:
            return None
        
        return found_items
    
    def search_files(self, name):
        """Search for files and return results"""
        found_items = self.find_file_or_folder(name, return_first=False)
        
        if not found_items:
            return f"I couldn't find any files or folders matching {name}"
        
        if len(found_items) == 1:
            return f"I found {name} at: {found_items[0]}"
        
        # Multiple results
        result = f"I found {len(found_items)} items matching {name}:\n"
        for i, item in enumerate(found_items[:5], 1):  # Limit to 5 results
            result += f"{i}. {item}\n"
        
        if len(found_items) > 5:
            result += f"... and {len(found_items) - 5} more"
        
        return result
    
    def get_file_info(self, name):
        """Get information about a file"""
        try:
            found_path = self.find_file_or_folder(name, return_first=True)
            
            if not found_path:
                return f"I couldn't find {name} to get information about."
            
            # Get file stats
            stats = os.stat(found_path)
            size_bytes = stats.st_size
            
            # Convert size to human-readable format
            if size_bytes < 1024:
                size_str = f"{size_bytes} bytes"
            elif size_bytes < 1024 * 1024:
                size_str = f"{size_bytes / 1024:.2f} KB"
            elif size_bytes < 1024 * 1024 * 1024:
                size_str = f"{size_bytes / (1024 * 1024):.2f} MB"
            else:
                size_str = f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"
            
            # Get dates
            created = datetime.fromtimestamp(stats.st_ctime).strftime("%Y-%m-%d %H:%M:%S")
            modified = datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            
            # Determine type
            if os.path.isdir(found_path):
                file_type = "Folder"
            else:
                file_type = f"File ({Path(found_path).suffix})"
            
            result = f"{name} information:\n"
            result += f"Type: {file_type}\n"
            result += f"Size: {size_str}\n"
            result += f"Created: {created}\n"
            result += f"Last Modified: {modified}\n"
            result += f"Location: {found_path}"
            
            return result
        
        except Exception as e:
            return f"I encountered an error getting information about {name}: {str(e)}"
    
    def rename_file_or_folder(self, old_name, new_name):
        """Rename a file or folder"""
        try:
            found_path = self.find_file_or_folder(old_name, return_first=True)
            
            if not found_path:
                return f"I couldn't find {old_name} to rename."
            
            parent_dir = os.path.dirname(found_path)
            new_path = os.path.join(parent_dir, new_name)
            
            if os.path.exists(new_path):
                return f"A file or folder named {new_name} already exists in that location."
            
            os.rename(found_path, new_path)
            return f"Successfully renamed {old_name} to {new_name}"
        
        except Exception as e:
            return f"I encountered an error renaming {old_name}: {str(e)}"
    
    def copy_file_or_folder(self, name, destination):
        """Copy a file or folder to a destination"""
        try:
            found_path = self.find_file_or_folder(name, return_first=True)
            
            if not found_path:
                return f"I couldn't find {name} to copy."
            
            dest_path = Path(destination)
            if not dest_path.exists():
                return f"The destination {destination} doesn't exist."
            
            if os.path.isdir(found_path):
                shutil.copytree(found_path, dest_path / os.path.basename(found_path))
            else:
                shutil.copy2(found_path, dest_path)
            
            return f"Successfully copied {name} to {destination}"
        
        except Exception as e:
            return f"I encountered an error copying {name}: {str(e)}"
    
    def move_file_or_folder(self, name, destination):
        """Move a file or folder to a destination"""
        try:
            found_path = self.find_file_or_folder(name, return_first=True)
            
            if not found_path:
                return f"I couldn't find {name} to move."
            
            dest_path = Path(destination)
            if not dest_path.exists():
                return f"The destination {destination} doesn't exist."
            
            shutil.move(found_path, dest_path)
            return f"Successfully moved {name} to {destination}"
        
        except Exception as e:
            return f"I encountered an error moving {name}: {str(e)}"
    
    def select_all_files_in_folder(self, folder_name):
        """Open a folder and select all files in it"""
        try:
            # Find the folder
            found_path = self.find_file_or_folder(folder_name, return_first=True)
            
            if not found_path:
                return f"I couldn't find folder {folder_name}"
            
            if not os.path.isdir(found_path):
                return f"{folder_name} is not a folder"
            
            if self.system == "Windows":
                # Open folder in Explorer and select all files
                # First, open the folder
                subprocess.Popen(f'explorer /select,"{found_path}"')
                
                # Wait a moment for the window to open
                import time
                time.sleep(0.5)
                
                # Send Ctrl+A to select all
                import pyautogui
                pyautogui.hotkey('ctrl', 'a')
                
                return f"Opened {folder_name} and selected all files"
            
            elif self.system == "Darwin":  # macOS
                # Open folder in Finder
                subprocess.run(["open", found_path])
                import time
                time.sleep(0.5)
                # Send Cmd+A to select all
                import pyautogui
                pyautogui.hotkey('command', 'a')
                return f"Opened {folder_name} and selected all files"
            
            else:  # Linux
                # Open folder
                subprocess.run(["xdg-open", found_path])
                import time
                time.sleep(0.5)
                # Send Ctrl+A to select all
                import pyautogui
                pyautogui.hotkey('ctrl', 'a')
                return f"Opened {folder_name} and selected all files"
        
        except ImportError:
            return f"PyAutoGUI is required for this feature. Please install it: pip install pyautogui"
        except Exception as e:
            return f"I encountered an error selecting files in {folder_name}: {str(e)}"
    
    def open_recycle_bin(self):
        """Open the Recycle Bin"""
        try:
            if self.system == "Windows":
                # Open Recycle Bin using shell command
                os.startfile("shell:RecycleBinFolder")
                return "Opening Recycle Bin for you"
            elif self.system == "Darwin":  # macOS
                subprocess.run(["open", os.path.expanduser("~/.Trash")])
                return "Opening Trash for you"
            else:  # Linux
                # Different Linux distributions have different trash locations
                trash_path = Path.home() / ".local/share/Trash"
                if trash_path.exists():
                    subprocess.run(["xdg-open", str(trash_path)])
                    return "Opening Trash for you"
                else:
                    return "I couldn't locate the Trash folder on your system"
        except Exception as e:
            return f"I encountered an error opening Recycle Bin: {str(e)}"
    
    def empty_recycle_bin(self):
        """Empty the Recycle Bin permanently"""
        try:
            if self.system == "Windows":
                # Use winshell to empty recycle bin
                if WINSHELL_AVAILABLE:
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
                    return "Successfully emptied the Recycle Bin. All files have been permanently deleted."
                else:
                    # Fallback method using PowerShell
                    cmd = 'Clear-RecycleBin -Force -ErrorAction SilentlyContinue'
                    subprocess.run(["powershell", "-Command", cmd], check=True)
                    return "Successfully emptied the Recycle Bin. All files have been permanently deleted."
            elif self.system == "Darwin":  # macOS
                trash_path = Path.home() / ".Trash"
                if trash_path.exists():
                    for item in trash_path.iterdir():
                        if item.is_dir():
                            shutil.rmtree(item)
                        else:
                            item.unlink()
                    return "Successfully emptied the Trash. All files have been permanently deleted."
            else:  # Linux
                trash_path = Path.home() / ".local/share/Trash/files"
                if trash_path.exists():
                    for item in trash_path.iterdir():
                        if item.is_dir():
                            shutil.rmtree(item)
                        else:
                            item.unlink()
                    return "Successfully emptied the Trash. All files have been permanently deleted."
            
            return "Recycle Bin emptied successfully"
        
        except Exception as e:
            return f"I encountered an error emptying Recycle Bin: {str(e)}"
    
    def get_recycle_bin_info(self):
        """Get information about Recycle Bin contents"""
        try:
            if self.system == "Windows":
                if WINSHELL_AVAILABLE:
                    items = list(winshell.recycle_bin())
                    if not items:
                        return "The Recycle Bin is empty"
                    
                    total_size = sum(item.size() for item in items if hasattr(item, 'size'))
                    
                    # Convert size to human-readable format
                    if total_size < 1024:
                        size_str = f"{total_size} bytes"
                    elif total_size < 1024 * 1024:
                        size_str = f"{total_size / 1024:.2f} KB"
                    elif total_size < 1024 * 1024 * 1024:
                        size_str = f"{total_size / (1024 * 1024):.2f} MB"
                    else:
                        size_str = f"{total_size / (1024 * 1024 * 1024):.2f} GB"
                    
                    return f"The Recycle Bin contains {len(items)} items, total size: {size_str}"
                else:
                    return "Recycle Bin information is available. Use 'open recycle bin' to view contents."
            else:
                return "Recycle Bin information feature is currently only available on Windows"
        
        except Exception as e:
            return f"I encountered an error getting Recycle Bin info: {str(e)}"


# Global instance
file_manager = FileManager()


# Wrapper functions for easy access
def OpenFileOrFolder(name):
    return file_manager.open_file_or_folder(name)


def DeleteFileOrFolder(name, confirmed=True):
    return file_manager.delete_file_or_folder(name, confirmed)


def CreateFolder(folder_name, location=None):
    return file_manager.create_folder(folder_name, location)


def SearchFiles(name):
    return file_manager.search_files(name)


def GetFileInfo(name):
    return file_manager.get_file_info(name)


def RenameFileOrFolder(old_name, new_name):
    return file_manager.rename_file_or_folder(old_name, new_name)


def CopyFileOrFolder(name, destination):
    return file_manager.copy_file_or_folder(name, destination)


def MoveFileOrFolder(name, destination):
    return file_manager.move_file_or_folder(name, destination)


def OpenRecycleBin():
    return file_manager.open_recycle_bin()


def EmptyRecycleBin():
    return file_manager.empty_recycle_bin()


def GetRecycleBinInfo():
    return file_manager.get_recycle_bin_info()


def SelectAllFilesInFolder(folder_name):
    return file_manager.select_all_files_in_folder(folder_name)
