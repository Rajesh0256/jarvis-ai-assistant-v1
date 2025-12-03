"""
Vision Analysis Module for Jarvis AI
Analyzes images, screenshots, documents, and visual data
Uses Groq's vision-capable models
"""

import base64
import os
from groq import Groq
from dotenv import dotenv_values
from PIL import Image
import io

env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey", "")
Username = env_vars.get("Username", "User")
Assistantname = env_vars.get("Assistantname", "Jarvis")

if not GroqAPIKey:
    print("Warning: GroqAPIKey not found in .env file")
    GroqAPIKey = "dummy_key"

client = Groq(api_key=GroqAPIKey)


def encode_image_to_base64(image_path):
    """Convert image to base64 string"""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        print(f"Error encoding image: {e}")
        return None


def optimize_image(image_path, max_size=(1024, 1024)):
    """Optimize image size for faster processing"""
    try:
        img = Image.open(image_path)
        
        # Convert to RGB if necessary
        if img.mode in ('RGBA', 'LA', 'P'):
            img = img.convert('RGB')
        
        # Resize if too large
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # Save optimized version
        optimized_path = image_path.replace('.', '_optimized.')
        img.save(optimized_path, 'JPEG', quality=85, optimize=True)
        
        return optimized_path
    except Exception as e:
        print(f"Error optimizing image: {e}")
        return image_path


def AnalyzeImage(image_path, query="What do you see in this image?"):
    """
    Analyze an image and answer questions about it
    
    Args:
        image_path: Path to the image file
        query: Question about the image
    
    Returns:
        Analysis result as string
    """
    try:
        print(f"Analyzing image: {image_path}")
        
        # Check if file exists
        if not os.path.exists(image_path):
            return f"I couldn't find the image at {image_path}. Please check the path."
        
        # Optimize image for faster processing
        optimized_path = optimize_image(image_path)
        
        # Encode image to base64
        image_base64 = encode_image_to_base64(optimized_path)
        
        if not image_base64:
            return "I couldn't process the image. Please try another image."
        
        # Create vision prompt
        system_prompt = f"""You are {Assistantname}, an AI assistant with vision capabilities.
Analyze images carefully and provide accurate, detailed descriptions.
Be helpful and answer the user's questions about the image clearly."""

        # Use Groq's vision model (llama-3.2-90b-vision-preview or similar)
        completion = client.chat.completions.create(
            model="llama-3.2-90b-vision-preview",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": query
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_base64}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=1024,
            temperature=0.7
        )
        
        result = completion.choices[0].message.content.strip()
        
        # Clean up optimized image
        if optimized_path != image_path and os.path.exists(optimized_path):
            try:
                os.remove(optimized_path)
            except:
                pass
        
        return result
        
    except Exception as e:
        print(f"Error analyzing image: {e}")
        return f"I encountered an error while analyzing the image: {str(e)}"


def ReadTextFromImage(image_path):
    """
    Extract and read text from an image (OCR)
    
    Args:
        image_path: Path to the image file
    
    Returns:
        Extracted text as string
    """
    query = """Please extract and read all the text visible in this image.
List the text exactly as it appears, maintaining the structure and formatting where possible."""
    
    return AnalyzeImage(image_path, query)


def AnalyzeScreenshot(image_path, query="What does this screenshot show?"):
    """
    Analyze a screenshot and explain what it shows
    
    Args:
        image_path: Path to the screenshot
        query: Question about the screenshot
    
    Returns:
        Analysis result as string
    """
    enhanced_query = f"""This is a screenshot. {query}
Please provide a clear explanation of what you see, including any text, UI elements, or important details."""
    
    return AnalyzeImage(image_path, enhanced_query)


def AnalyzeDocument(image_path, query="Summarize this document"):
    """
    Analyze a document image (PDF page, scanned document, etc.)
    
    Args:
        image_path: Path to the document image
        query: What to do with the document
    
    Returns:
        Analysis result as string
    """
    enhanced_query = f"""This is a document image. {query}
Please read the document carefully and provide the requested information."""
    
    return AnalyzeImage(image_path, enhanced_query)


def FindInformationInImage(image_path, information_type):
    """
    Find specific information in an image
    
    Args:
        image_path: Path to the image
        information_type: What to find (e.g., "due date", "price", "phone number")
    
    Returns:
        Found information as string
    """
    query = f"""Please find and extract the {information_type} from this image.
If you find it, state it clearly. If not found, say so."""
    
    return AnalyzeImage(image_path, query)


def ExplainErrorMessage(image_path):
    """
    Explain an error message shown in an image
    
    Args:
        image_path: Path to the error screenshot
    
    Returns:
        Explanation of the error
    """
    query = """This image shows an error message. Please:
1. Read the error message
2. Explain what it means in simple terms
3. Suggest possible solutions or next steps"""
    
    return AnalyzeImage(image_path, query)


def CompareImages(image_path1, image_path2):
    """
    Compare two images and describe differences
    
    Args:
        image_path1: Path to first image
        image_path2: Path to second image
    
    Returns:
        Comparison result as string
    """
    # Analyze both images separately
    result1 = AnalyzeImage(image_path1, "Describe this image in detail.")
    result2 = AnalyzeImage(image_path2, "Describe this image in detail.")
    
    comparison = f"""Comparison of two images:

Image 1:
{result1}

Image 2:
{result2}

Based on these descriptions, the images show different content."""
    
    return comparison


# Supported image formats
SUPPORTED_FORMATS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']


def is_supported_image(file_path):
    """Check if file is a supported image format"""
    ext = os.path.splitext(file_path)[1].lower()
    return ext in SUPPORTED_FORMATS


if __name__ == "__main__":
    print("Vision Analysis Module Test")
    print("=" * 70)
    print("\nThis module can:")
    print("1. Analyze images and answer questions")
    print("2. Read text from images (OCR)")
    print("3. Analyze screenshots")
    print("4. Analyze documents")
    print("5. Find specific information in images")
    print("6. Explain error messages")
    print("\nSupported formats:", ", ".join(SUPPORTED_FORMATS))
