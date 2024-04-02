import pyttsx3
import pyaudio
import speech_recognition as sr
import webbrowser
import os
import subprocess
import datetime
engine = pyttsx3.init()
audio = sr.Recognizer()
text = ''
from googlesearch import search
import sys


voice = engine.getProperty('voices')
engine.setProperty('volume', 1)
engine.setProperty('voice', voice[1].id)
def listener():
           try:
                while True:
                        with sr.Microphone() as source:
                                print("speak....")
                                audio_textlisten = audio.listen(source)
                                global text
                                text = audio.recognize_google(audio_textlisten)
                                return text.lower()
           except sr.UnknownValueError:
                  os.system("python C:/Users/Dell/python-projects/pythonproject5/jarvis.py")
def open_youtube():
        os.system("start https://www.youtube.com/")
        engine.say("opening youtube")
        engine.runAndWait()
        query.replace('youtube', '')
def open_whatsapp():
        os.system("start https://web.whatsapp.com/")
        engine.say("opening whatsapp")
        engine.runAndWait()
        query.replace('whatsapp', '')
def searching():
        searchresult = search(query,num_results=50,advanced=True,lang="english")
        for seaches in searchresult:
                print(seaches['discription'])
        engine.say("searching")
        engine.runAndWait()
def open_pw():
        os.system("start https://www.pw.live/study/batches/udaan-2025-645851/batch-overview?came_from=my-batches")
        engine.say("opening pw")
        engine.runAndWait()
        query.replace('pw', '')

def sleep_laptop():
    if os.name == "nt":
        os.system("shutdown /s /t 1")  # /s flag for shutdown, /t 1 for a delay of 1 second
    elif os.name == "posix":
         os.system("pmset sleepnow")
        
def wishme():
     time = int(datetime.datetime.now().hour) 
     if time > 0 and time < 12:
        engine.say("good morning")
        engine.runAndWait()
     elif time > 12 and time < 15:
        engine.say("good afternoon")
        engine.runAndWait()
     else:
        engine.say("good evening")
        engine.runAndWait()
if __name__ == "__main__":
    while True:
         listener()
        
         if 'assistant'in text:
                        wishme()
                       
                        
         while True:
                query = listener()
                if 'youtube' in query:
                        open_youtube()
                elif 'whatsapp' in query:
                        open_whatsapp()
                elif 'what time is it' in query:
                        time = datetime.datetime.now().strftime('%I:%M %p')
                        print(time)
                        engine.say(time)
                        engine.runAndWait()
                elif 'quit' in query:
                        engine.say("thanks for using me")
                        engine.runAndWait()
                        sys.exit()
                elif 'search' in query:
                          engine.say("what do you want to search")
                          engine.runAndWait()
                          query.replace('search', '')
                          searching()
                elif 'pw' in query:
                      open_pw()           
                elif 'shutdown' in query:
                       os.system("shutdown /s")
                elif 'sleep' in query:
                       sleep_laptop()