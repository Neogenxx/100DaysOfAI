import pyttsx3
import os

def init_tts_engine(voice_gender='male'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    return engine

if __name__ == "__main__":
    try:
        engine = init_tts_engine('male')  # or 'female'
        text = "Welcome to Day 8 of the 100 Days of AI!"
        engine.say(text)
        engine.save_to_file(text, "output_audio.mp3")
        engine.runAndWait()  # Run both say + save in a single loop
    finally:
        try:
            engine.stop()
        except Exception:
            pass
        os._exit(0)

