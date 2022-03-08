#PiDash Project
#2022 - Angelo Poggi angelo.poggi@enigmaconsulting.tech
import gpiozero
from gpiozero import *

class PiDash:
    def pulsegenread(self):
        sen0105 = gpiozero.DigitalInputDevice(26,pull_up=True)
        speedReading = 0
        while True:
            if sen0105.value == 1:
                speedReading += 1
                if speedReading >= 16000:
                    print(speedReading // 16000)
            elif sen0105.value == 0:
                #reset speed reading back to zero if no movement
                speedReading = 0


