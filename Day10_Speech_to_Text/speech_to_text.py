import speech_recognition as sr
import os

def transcribe_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🎙️ Say something... (Press Ctrl+C to stop)\n")

    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)
        print("🧠 Recognizing...\n")
        text = recognizer.recognize_google(audio, language="en-IN")
        print("📝 Transcribed Text:\n", text)

        # Get current directory and save text file there
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "transcription.txt")

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)

        print(f"\n✅ Transcription saved to '{file_path}'.")

    except sr.UnknownValueError:
        print("❌ Sorry, could not understand the audio.")
    except sr.RequestError as e:
        print(f"❌ Could not request results from Google Speech Recognition service; {e}")
    except sr.WaitTimeoutError:
        print("⌛ Listening timed out while waiting for phrase to start.")
    except KeyboardInterrupt:
        print("\n🛑 Process manually stopped.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    transcribe_speech()
