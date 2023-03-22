# importing the module
import wikipedia as wp

# finding result for the search
# sentences = 2 refers to numbers of line
#result = wikipedia.summary("India", sentences = 2)
import speech_recognition
import pyaudio
# Obtain audio from the microphone
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

# Recognize speech using Google Speech Recognition
print("You said:")
said= recognizer.recognize_google(audio)
print(said)


print(wp.search(said, results = 20))
# printing the result

