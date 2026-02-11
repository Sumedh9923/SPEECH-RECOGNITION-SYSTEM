import speech_recognition as sr

# Create recognizer object
recognizer = sr.Recognizer()

# Audio file name (make sure this file exists in same folder)
audio_file = "converted_audio.wav"

try:
    # Load audio file
    with sr.AudioFile(audio_file) as source:
        print("Listening to audio file...")
        audio_data = recognizer.record(source)

    print("Transcribing...")

    # Convert speech to text using Google API
    text = recognizer.recognize_google(audio_data)

    print("\n✅ Recognized Text:")
    print(text)

except FileNotFoundError:
    print("❌ Audio file not found. Check file name.")

except sr.UnknownValueError:
    print("❌ Could not understand the audio.")

except sr.RequestError as e:
    print(f"❌ API request failed: {e}")
