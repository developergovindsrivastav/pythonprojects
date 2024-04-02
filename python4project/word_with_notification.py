import requests
import time
from plyer import notification
import pyttsx3
url = "https://randomhistoricalfact.000webhostapp.com/fact"
text_speech = pyttsx3.init()
newVoiceRate = 130
text_speech.setProperty('rate',newVoiceRate)
voices = text_speech.getProperty('voices')
text_speech.setProperty('voice', voices[1].id)


def main():
    while True:
        try:
            response1 = requests.get(url)
            response2 = response1.json()
        except:
            print("Something went wrong")
        if len(response2["fact"]) <= 256:
            if response2["fact"] == None:
                print("Sorry, no fact found")
            else:
                notification.notify(
                    title = "History Fact",
                    message = response2["fact"],
                    app_name = "Word with Notification",
                    timeout = 120,
                    app_icon=r"C:\Users\Dell\python-projects\python4project/king.ico"
                )
                text_speech.say(response2["fact"])
                text_speech.runAndWait()
                time.sleep(60*60)
        else:
            main()        
if __name__ == "__main__":
    main()