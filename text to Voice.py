import gtts

text = "Uta ayta"
tts = gtts.gTTS(text=text, lang='kn')
tts.save("output.mp3")
# from gtts.lang import tts_langs

# print(tts_langs())
