"""
Server Client for Jarvis
Handles communication with backend server instead of direct API calls
"""

import requests
import os
from dotenv import load_dotenv

load_dotenv()

class ServerClient:
    def __init__(self):
        # Check if user wants to use server or local API keys
        self.use_server = os.getenv("USE_SERVER", "true").lower() == "true"
        self.server_url = os.getenv("SERVER_URL", "http://localhost:5000")
        
        # Fallback to local API keys if server is disabled
        if not self.use_server:
            self.groq_api_key = os.getenv("GROQ_API_KEY")
            self.google_api_key = os.getenv("GOOGLE_API_KEY")
    
    def check_server_health(self):
        """Check if server is online"""
        try:
            response = requests.get(f"{self.server_url}/health", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def send_chat_request(self, message, conversation_history=[]):
        """Send chat request to server"""
        try:
            response = requests.post(
                f"{self.server_url}/api/chat",
                json={
                    "message": message,
                    "history": conversation_history
                },
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get("response", "")
            else:
                return f"Server error: {response.status_code}"
                
        except requests.exceptions.ConnectionError:
            return "Cannot connect to server. Please check if server is running."
        except requests.exceptions.Timeout:
            return "Request timeout. Server is taking too long to respond."
        except Exception as e:
            return f"Error: {str(e)}"
    
    def send_vision_request(self, image_data, prompt="Describe this image"):
        """Send vision analysis request to server"""
        try:
            response = requests.post(
                f"{self.server_url}/api/vision",
                json={
                    "image": image_data,
                    "prompt": prompt
                },
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get("response", "")
            else:
                return f"Server error: {response.status_code}"
                
        except Exception as e:
            return f"Error: {str(e)}"
    
    def get_server_stats(self):
        """Get server usage statistics"""
        try:
            response = requests.get(f"{self.server_url}/api/stats", timeout=5)
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None
