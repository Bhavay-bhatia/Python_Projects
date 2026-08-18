import time 
from plyer import notification

while True:
    print("sip some water !!")
    notification.notify(title="Drinking water reminder",message="please drink some water !!")
    time.sleep(60*60)
    