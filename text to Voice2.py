import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'english')
engine.say("Hello, world!")
engine.save_to_file("output.mp3")