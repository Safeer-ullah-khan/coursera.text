import datetime
import time
import winsound

user=input("Set time for alarm in HH:MM (24 hour formate)")
print(f"Alarm time is {user}....")

while True:
    now=datetime.datetime.now().strftime("%H:%M")
    if(now==user):
        print("⏰wake up alarm time reached")
        for i in range(5):
            winsound.Beep(1000,500)
        break
    time.sleep(1)

