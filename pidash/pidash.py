#PiDash Project
#2022 - Angelo Poggi angelo.poggi@enigmaconsulting.tech
import gpiozero
from gpiozero import *

class PiDash:
    def pulsegenread(self):
        sen0105 = gpiozero.DigitalInputDevice(26,pull_up=True)
        while True:
            speedReading = sen0105.value ++ sen0105.value
            if speedReading >= 16000:
                print(speedReading / 16000)

