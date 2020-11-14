import pyttsx3

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)
name = input("What's your name? ")
engine.say(f"hello, {name}")
engine.runAndWait()