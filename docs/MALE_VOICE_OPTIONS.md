# Male Voice Options for Jarvis 🎤

## Current Setting
Your Jarvis is now configured to use: **`hi-IN-MadhurNeural`** (Male Hindi voice)

---

## Available Male Voices

### Hindi (India) - Recommended for You
```
AssistantVoice=hi-IN-MadhurNeural
```
- **Language:** Hindi (India)
- **Gender:** Male
- **Quality:** High quality, natural sounding
- **Best for:** Hindi speakers

---

### English Male Voices

#### 1. English (US) - Guy (Recommended)
```
AssistantVoice=en-US-GuyNeural
```
- **Accent:** American English
- **Tone:** Professional, clear
- **Best for:** General use, professional assistant

#### 2. English (US) - Eric
```
AssistantVoice=en-US-EricNeural
```
- **Accent:** American English
- **Tone:** Friendly, casual
- **Best for:** Casual conversations

#### 3. English (US) - Davis
```
AssistantVoice=en-US-DavisNeural
```
- **Accent:** American English
- **Tone:** Deep, authoritative
- **Best for:** Professional, serious tone

#### 4. English (US) - Tony
```
AssistantVoice=en-US-TonyNeural
```
- **Accent:** American English
- **Tone:** Energetic, young
- **Best for:** Dynamic interactions

#### 5. English (UK) - Ryan
```
AssistantVoice=en-GB-RyanNeural
```
- **Accent:** British English
- **Tone:** Professional, sophisticated
- **Best for:** British accent preference

#### 6. English (UK) - Thomas
```
AssistantVoice=en-GB-ThomasNeural
```
- **Accent:** British English
- **Tone:** Clear, articulate
- **Best for:** Formal British accent

#### 7. English (Australia) - William
```
AssistantVoice=en-AU-WilliamNeural
```
- **Accent:** Australian English
- **Tone:** Friendly, casual
- **Best for:** Australian accent preference

#### 8. English (India) - Prabhat
```
AssistantVoice=en-IN-PrabhatNeural
```
- **Accent:** Indian English
- **Tone:** Clear, professional
- **Best for:** Indian English accent

---

## How to Change Voice

### Method 1: Edit .env File
1. Open `.env` file
2. Find the line: `AssistantVoice=hi-IN-MadhurNeural`
3. Replace with your preferred voice
4. Save the file
5. Restart Jarvis

### Method 2: Direct Edit
```properties
# Current (Male Hindi)
AssistantVoice=hi-IN-MadhurNeural

# Change to Male American English
AssistantVoice=en-US-GuyNeural

# Change to Male British English
AssistantVoice=en-GB-RyanNeural

# Change to Deep American Voice
AssistantVoice=en-US-DavisNeural
```

---

## Voice Characteristics Comparison

| Voice | Language | Accent | Tone | Best For |
|-------|----------|--------|------|----------|
| **hi-IN-MadhurNeural** | Hindi | Indian | Professional | Hindi speakers |
| **en-US-GuyNeural** | English | American | Professional | General use |
| **en-US-DavisNeural** | English | American | Deep | Authority |
| **en-GB-RyanNeural** | English | British | Sophisticated | British accent |
| **en-IN-PrabhatNeural** | English | Indian | Clear | Indian English |

---

## Testing Voices

### Test Current Voice:
```python
from Backend.TextToSpeech import TextToSpeech

# Test the voice
TextToSpeech("Hello sir, I am Jarvis, your personal assistant")
```

### Test Different Voices:
1. Change `AssistantVoice` in `.env`
2. Restart Python
3. Run the test above
4. Compare and choose your favorite

---

## Popular Combinations

### For Professional Assistant (English):
```properties
AssistantVoice=en-US-GuyNeural
InputLanguage=en-US
```

### For British Butler Style:
```properties
AssistantVoice=en-GB-RyanNeural
InputLanguage=en-GB
```

### For Deep Authoritative Voice:
```properties
AssistantVoice=en-US-DavisNeural
InputLanguage=en-US
```

### For Hindi Assistant (Current):
```properties
AssistantVoice=hi-IN-MadhurNeural
InputLanguage=hi-IN
```

---

## Voice Customization

### Adjust Pitch:
In `Backend/TextToSpeech.py`, line 13:
```python
communicate = edge_tts.Communicate(text, AssistantVoice, pitch='+5Hz', rate='+13%')
```

**Options:**
- **Lower pitch (deeper):** `pitch='-5Hz'` or `pitch='-10Hz'`
- **Higher pitch:** `pitch='+10Hz'` or `pitch='+15Hz'`
- **Normal pitch:** `pitch='+0Hz'`

### Adjust Speed:
```python
communicate = edge_tts.Communicate(text, AssistantVoice, pitch='+5Hz', rate='+13%')
```

**Options:**
- **Slower:** `rate='+0%'` or `rate='-10%'`
- **Faster:** `rate='+20%'` or `rate='+30%'`
- **Normal:** `rate='+13%'` (current)

---

## Recommended Settings

### For Movie-Style Jarvis (Iron Man):
```properties
AssistantVoice=en-GB-RyanNeural  # British accent like J.A.R.V.I.S.
```
```python
# In TextToSpeech.py
pitch='+0Hz'  # Normal pitch
rate='+10%'   # Slightly faster
```

### For Deep Professional Voice:
```properties
AssistantVoice=en-US-DavisNeural
```
```python
# In TextToSpeech.py
pitch='-5Hz'  # Deeper voice
rate='+5%'    # Slower, more authoritative
```

### For Friendly Assistant:
```properties
AssistantVoice=en-US-EricNeural
```
```python
# In TextToSpeech.py
pitch='+5Hz'  # Current setting
rate='+13%'   # Current setting
```

---

## Troubleshooting

### Voice Not Changing:
1. Make sure you saved the `.env` file
2. Restart Jarvis completely
3. Check for typos in voice name
4. Verify internet connection (Edge TTS requires internet)

### Voice Sounds Wrong:
1. Try different pitch settings
2. Adjust rate (speed)
3. Test multiple voices to find your preference

### No Audio:
1. Check system volume
2. Verify speakers/headphones connected
3. Test with: `python -c "from Backend.TextToSpeech import TextToSpeech; TextToSpeech('test')"`

---

## Quick Test Script

Create `test_voice.py`:
```python
from Backend.TextToSpeech import TextToSpeech

# Test messages
messages = [
    "Hello sir, I am Jarvis",
    "Instagram opening sir",
    "downloads folder opening sir",
    "Weather in New York: Clear, 20 degrees",
]

for msg in messages:
    print(f"Speaking: {msg}")
    TextToSpeech(msg)
    print("Done!\n")
```

Run: `python test_voice.py`

---

## Current Configuration

Your current settings:
```properties
Username=rajes
Assistantname=Friday
InputLanguage=hi-IN
AssistantVoice=hi-IN-MadhurNeural  ← Male Hindi Voice
```

---

## Summary

✅ **Changed to Male Voice:** `hi-IN-MadhurNeural`
✅ **Language:** Hindi (India)
✅ **Gender:** Male
✅ **Quality:** High quality neural voice

To test, restart Jarvis and say any command. You'll hear the male voice!

---

## Popular Male Voice Recommendations

1. **For Hindi:** `hi-IN-MadhurNeural` (Current) ⭐
2. **For English (US):** `en-US-GuyNeural` ⭐
3. **For British Accent:** `en-GB-RyanNeural` ⭐
4. **For Deep Voice:** `en-US-DavisNeural` ⭐
5. **For Indian English:** `en-IN-PrabhatNeural` ⭐

Choose the one that fits your preference! 🎤
