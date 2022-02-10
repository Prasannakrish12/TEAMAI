import pyttsx3
import datetime
import speech_recognition as sr

teamai=pyttx3.init('sapi5')
voices=teamai.getProperty('voices')
teamai.setProperty('voice',voices[0].id)

def speak(audio):
    teamai.say(audio)
    teamai.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("welcome")
    elif hour<=12 and hour<18:
        speak("Have a safe journey")
    else:
        speak("enjoy your journey")



if__name__as"__main__":
   wishme()                    
