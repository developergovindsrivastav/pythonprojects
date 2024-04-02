import os
import sys
import datetime
import pyttsx3
import speech_recognition as sr
from googlesearch import search

engine = pyttsx3.init()
audio = sr.Recognizer()

voice = engine.getProperty('voices')
engine.setProperty('volume', 1)
engine.setProperty('voice', voice[1].id)

def listener():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio_text = audio.listen(source)
            text = audio.recognize_google(audio_text)
            print("You said:", text)
            return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

def open_website(url, message):
    os.system(f"start {url}")
    engine.say(message)
    engine.runAndWait()

def search_google(query):
    search_results = search(query, num_results=5, lang="en")
    for result in search_results:
        print(result)

def sleep_laptop():
    if os.name == "nt":
        os.system("shutdown /h")
    elif os.name == "posix":
        os.system("pmset sleepnow")

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        engine.say("Good morning!")
    elif 12 <= hour < 18:
        engine.say("Good afternoon!")
    else:
        engine.say("Good evening!")
    engine.runAndWait()

def main():
    wish_me()
    while True:
        query = listener()
        if 'youtube' in query:
            open_website("https://www.youtube.com/", "Opening YouTube")
        elif 'whatsapp' in query:
            open_website("https://web.whatsapp.com/", "Opening WhatsApp")
        elif 'time' in query:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            print("Current time:", current_time)
            engine.say(f"The current time is {current_time}")
            engine.runAndWait()
        elif 'quit' in query:
            engine.say("Thanks for using me!")
            engine.runAndWait()
            sys.exit()
        elif 'search' in query:
            engine.say("What do you want to search?")
            engine.runAndWait()
            query = listener()
            search_google(query)
        elif 'pw' in query:
            open_website("https://www.pw.live/study/batches/udaan-2025-645851/batch-overview?came_from=my-batches", "Opening PW")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'sleep' in query:
            sleep_laptop()

if __name__ == "__main__":
    main()
