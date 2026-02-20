import os
import threading

class TTSEngine:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(TTSEngine, cls).__new__(cls)
            return cls._instance

    def speak(self, text):
        if not text:
            return
        
        # Clean the text to prevent terminal command errors
        clean_text = text.replace("'", "").replace('"', "")
        print(f">>> [TTS] Speaking: {clean_text}")
        
        try:
            # Bypass pyttsx3 and use macOS's native 'say' command
            os.system(f"say '{clean_text}'")
        except Exception as e:
            print(f"!!! [TTS] Error during speech: {e}")

# Global instance for easy access
tts_engine = TTSEngine()

def speak(text):
    tts_engine.speak(text)