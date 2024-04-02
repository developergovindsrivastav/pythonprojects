import time
from plyer import notification
water_quantity = 0
import pyttsx3
text_converter = pyttsx3.init()

def water_reminder():
    global water_quantity 
    while True:
        water_quantity += 250 
        notification.notify(
            title="**IMPORTANT!!** \n It's time to drink some water",
            message=f"You have consumed {water_quantity} ml of water today. Keep it up!",
            timeout=10,
            app_icon=r"C:\Users\Dell\python-projects\python3project\icon.ico"
        )
        text_converter.say(f" please drink water!You have consumed {water_quantity} ml of water today. Keep it up!")
        text_converter.runAndWait()
        time.sleep(60*60)

water_reminder()






