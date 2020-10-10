import pyttsx3 #pip install pyttsx3
import datetime

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    speak("This is Jarvis")