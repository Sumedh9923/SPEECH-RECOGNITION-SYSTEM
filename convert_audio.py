from pydub import AudioSegment

# Replace this with your mobile file name
input_file = "sample.wav"

print("Loading audio...")
audio = AudioSegment.from_file(input_file)

print("Converting to mono and 16kHz...")
audio = audio.set_channels(1)
audio = audio.set_frame_rate(16000)

print("Exporting as WAV...")
audio.export("converted_audio.wav", format="wav")

print("✅ Audio converted successfully!")
