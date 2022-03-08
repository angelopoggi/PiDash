#PiDash Project
#2022 - Angelo Poggi angelo.poggi@enigmaconsulting.tech
import gpiozero
from gpiozero import *

class PiDash:
    #space for Init function if needed
    def __init__(self):
    def pulsegenread(self):
        sen0105 = gpiozero.DigitalInputDevice(2,pull_up=False)
        while True:
            print(sen0105)
