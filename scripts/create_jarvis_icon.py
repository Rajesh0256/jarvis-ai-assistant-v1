"""
Create Jarvis system tray icon
"""
from PIL import Image, ImageDraw, ImageFont
import os

# Create icon
img = Image.new('RGB', (128, 128), color=(0, 150, 255))
draw = ImageDraw.Draw(img)

# Draw circle background
draw.ellipse([10, 10, 118, 118], fill=(0, 100, 200), outline=(255, 255, 255), width=3)

# Draw 'J' letter
try:
    font = ImageFont.truetype('arial.ttf', 70)
except:
    try:
        font = ImageFont.truetype('Arial.ttf', 70)
    except:
        font = ImageFont.load_default()

draw.text((40, 25), 'J', fill=(255, 255, 255), font=font)

# Ensure directory exists
os.makedirs('Frontend/Graphics', exist_ok=True)

# Save icon
img.save('Frontend/Graphics/jarvis_icon.png')
print("✅ Jarvis icon created: Frontend/Graphics/jarvis_icon.png")
