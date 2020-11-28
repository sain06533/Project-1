
import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia#pip install wikipedia

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

name = input("What's your name? ")
engine.say(f"Hello! {name}")

def wishme():
    speak("I am Destiny, and I am here to help you out on your day")
    speak("The current time is")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <=12:
        speak(f"Good Morning {name}")
    elif hour >= 12 and hour <= 18:
        speak(f"Good Afternoon {name}")
    elif hour >= 18 and hour <= 22:
        speak(f"Good Eveving {name}")
    elif hour >= 22 and hour <= 24:
        speak(f"Hey {name}, I think it's time to go to bed!")
    else:
        speak("Good Night")


    speak("Would you like a Rain Check?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recoginzing....")
            query = r.recognize_google(audio, 'en=US')
            print(query)
        except Exception as e:
            print(e)
            speak(f"I'm sorry, I couldn't recognise your voice {name}, Would you mind Saying it again?")

            return "None"

    return query

if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
                quit()
        elif "wikipedia" in query:
            speak("Searching....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
