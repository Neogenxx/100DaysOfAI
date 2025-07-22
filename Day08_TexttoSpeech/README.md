# Day 8: Text-to-Speech App (TTS using pyttsx3)

## 📌 Project Overview

This project demonstrates a simple offline Text-to-Speech (TTS) system using Python and the `pyttsx3` library. It reads a hardcoded text aloud and saves the speech as an `.mp3` file. This is a foundational step toward building AI-powered audio applications.

## 📚 Libraries Used

- `pyttsx3` — Offline text-to-speech conversion engine
- `os` — For forcefully exiting the script to prevent terminal hang issues

## 🔧 Key Functions

### `init_tts_engine(voice_gender='male')`
Initializes the TTS engine with default properties like speech rate. (The `voice_gender` parameter is currently unused.)

### `engine.say(text)`
Triggers the engine to speak the given text aloud.

### `engine.save_to_file(text, filename)`
Converts text to speech and saves it as an audio file (`output_audio.mp3`).

### `engine.runAndWait()`
Executes both speech output and file saving.

### `engine.stop()` and `os._exit(0)`
Gracefully shuts down the engine and forcefully exits to avoid terminal hang issues in some systems.

## ▶️ How to Run

1. Activate your virtual environment.
2. Install the required library:
   ```bash
   pip install pyttsx3
3. Run the script:
   ```bash
   python text_to_speech.py
