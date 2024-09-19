import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'english')
engine.say("Hello, world!")
engine.save_to_file('Hello, world!',"output1.mp3")
engine.runAndWait()