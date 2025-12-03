import pygame
import random
import asyncio
import edge_tts
import os
import threading
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
AssistantVoice = env_vars.get("AssistantVoice")

# Cache for faster subsequent responses
_pygame_initialized = False

def init_pygame():
    """Initialize pygame mixer once"""
    global _pygame_initialized
    if not _pygame_initialized:
        try:
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
            _pygame_initialized = True
        except Exception as e:
            print(f"Error initializing pygame: {e}")

async def TextToAudioFile(text) -> None:
    file_path = r"Data\speech.mp3"

    # Don't delete the file - just overwrite it
    # This prevents "file not found" errors
    
    # Faster speech rate for quicker responses
    communicate = edge_tts.Communicate(text, AssistantVoice, pitch='+5Hz', rate='+30%')
    await communicate.save(r"Data\speech.mp3")

def TTS(Text, func=lambda r=None: True):
    """Optimized TTS with faster initialization"""
    try:
        # Stop any currently playing audio first
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        except:
            pass
        
        # Generate audio file
        asyncio.run(TextToAudioFile(Text))

        # Initialize pygame once
        init_pygame()

        # Small delay to ensure file is ready
        import time
        time.sleep(0.05)

        # Load and play immediately
        pygame.mixer.music.load(r"Data\speech.mp3")
        pygame.mixer.music.play()

        clock = pygame.time.Clock()

        # Wait for playback to finish
        while pygame.mixer.music.get_busy():
            if not func():
                break
            clock.tick(10)

        return True
        
    except Exception as e:
        print(f"Error in TTS: {e}")
        return False
        
    finally:
        try:
            func(False)
            pygame.mixer.music.stop()
        except Exception as e:
            pass  # Ignore errors in cleanup

def TextToSpeech(Text, func=lambda r=None: True):
    """Fast text-to-speech with smart truncation"""
    Data = str(Text).split(".")

    # Shorter, more natural responses
    responses = [
        "Check the screen for more details sir.",
        "More info on screen sir.",
        "Full details are on screen sir.",
        "See the screen for the rest sir.",
        "Check screen for complete answer sir.",
        "More on your screen sir."
    ]

    # Speak less for faster responses - only first 2 sentences for long text
    if len(Data) > 3 and len(Text) >= 200:
        # Get first 2 sentences
        first_sentences = ". ".join(Data[:2]) + ". " + random.choice(responses)
        TTS(first_sentences, func)
    elif len(Text) >= 500:
        # For very long text, just speak first sentence
        TTS(Data[0] + ". " + random.choice(responses), func)
    else:
        TTS(Text, func)


def TextToSpeechAsync(Text):
    """Non-blocking version - starts speaking in background"""
    thread = threading.Thread(target=TextToSpeech, args=(Text,), daemon=True)
    thread.start()
    return thread
# jar tumhala purna read karaich lavaich asel tr TTS cha use kara jar 4 or tya peksha line 
# jast lines text asel tr TTS use kra ani Short made read karacih asel tr texttosppech use kara  
if __name__ == "__main__":
    while True:
        TextToSpeech(input("Enter the text : "))