# 🗣️ Day 10: Real-time Speech-to-Text App

This Python project captures audio from your microphone in real time and transcribes it into text using the **Google Speech Recognition API**.

---

## 📦 Libraries Used

| Library              | Purpose                                  |
|----------------------|------------------------------------------|
| `speech_recognition` | Captures and processes voice input       |
| `pyaudio`            | Enables microphone access (dependency)   |
| `os`                 | Handles file saving                      |

---

## 🧠 Key Function

### `transcribe_speech()`
- Initializes the recognizer and microphone.
- Listens to the user's voice.
- Sends audio to Google’s API.
- Prints and saves the recognized text to `transcription.txt`.

---

## 📥 How to Install

```
pip install SpeechRecognition
pip install pipwin
pipwin install pyaudio
```

## 🚀 How to Run

```
python speech_to_text.py
```