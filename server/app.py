"""
Jarvis AI Assistant - Backend Server
This server handles AI requests so users don't need their own API keys
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from groq import Groq
import google.generativeai as genai

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow requests from Jarvis client

# Initialize AI clients with YOUR API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

groq_client = Groq(api_key=GROQ_API_KEY)
genai.configure(api_key=GOOGLE_API_KEY)

# Usage tracking (optional - to monitor costs)
usage_stats = {"total_requests": 0, "total_tokens": 0}


@app.route('/health', methods=['GET'])
def health_check():
    """Check if server is running"""
    return jsonify({"status": "online", "message": "Jarvis server is running"})


@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests from Jarvis"""
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No JSON data provided", "success": False}), 400
        
        user_message = data.get('message', '')
        conversation_history = data.get('history', [])
        
        if not user_message:
            return jsonify({"error": "No message provided"}), 400
        
        # Use Groq for chat - add system message if history is empty
        if not conversation_history:
            messages = [
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
                {"role": "user", "content": user_message}
            ]
        else:
            messages = conversation_history + [
                {"role": "user", "content": user_message}
            ]
        
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=2048,
            temperature=0.7,
            stream=False
        )
        
        if not response or not response.choices:
            return jsonify({"error": "No response from AI", "success": False}), 500
        
        ai_response = response.choices[0].message.content
        tokens_used = response.usage.total_tokens if hasattr(response, 'usage') and response.usage else 0
        
        # Track usage
        usage_stats["total_requests"] += 1
        usage_stats["total_tokens"] += tokens_used
        
        return jsonify({
            "response": ai_response,
            "success": True
        })
        
    except Exception as e:
        print(f"Chat error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e), "success": False}), 500


@app.route('/api/vision', methods=['POST'])
def vision_analysis():
    """Handle vision/image analysis requests"""
    try:
        data = request.json
        image_data = data.get('image', '')
        prompt = data.get('prompt', 'Describe this image')
        
        if not image_data:
            return jsonify({"error": "No image provided"}), 400
        
        # Use Google Gemini for vision
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([prompt, image_data])
        
        usage_stats["total_requests"] += 1
        
        return jsonify({
            "response": response.text,
            "success": True
        })
        
    except Exception as e:
        return jsonify({"error": str(e), "success": False}), 500


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get usage statistics (admin only)"""
    return jsonify(usage_stats)


if __name__ == '__main__':
    if not GROQ_API_KEY or not GOOGLE_API_KEY:
        print("ERROR: API keys not found in .env file!")
        print("Please add GROQ_API_KEY and GOOGLE_API_KEY to your .env file")
        exit(1)
    
    print("=" * 50)
    print("🚀 Jarvis Backend Server Starting...")
    print("=" * 50)
    print(f"✓ Groq API: Connected")
    print(f"✓ Google AI: Connected")
    print(f"✓ Server: http://localhost:5000")
    print("=" * 50)
    
    # Run server
    app.run(host='0.0.0.0', port=5000, debug=False)
