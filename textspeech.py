import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'kannada')
engine.setProperty('rate', 170)  # Speed of speech
engine.say("Hello, world!")
# engine.save_to_file('Hello, world!',"output1.mp3")
engine.runAndWait()