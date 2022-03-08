#PiDash Project
#2022 - Angelo Poggi angelo.poggi@enigmaconsulting.tech
import gpiozero
from gpiozero import *

class PiDash:
    def pulsegenread(self):
        sen0105 = gpiozero.DigitalInputDevice(26,pull_up=True)
        while True:
            if sen0105.value == 1:
                i = 0
                i ++ 1
                if i >= 16000:
                    print(f"{ i // 16000 } MPH")

