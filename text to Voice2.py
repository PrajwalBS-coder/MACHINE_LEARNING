import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Get the available voices
voices = engine.getProperty('voices')

# Print available voices
for idx, voice in enumerate(voices):
    print(f"Voice {idx}: {voice.name}, ID: {voice.id}")

# Select the specific voice by setting its ID (choose from the printed list)
engine.setProperty('voice', voices[0].id)  # Example: selecting the second voice

# Set speech rate (optional)
engine.setProperty('rate', 160)  # Speed of speech

# Set volume (optional)
engine.setProperty('volume', 1)  # 1.0 is max

# Convert text to speech
engine.say("Hello, how are you doing?")

# Play the speech
engine.runAndWait()
