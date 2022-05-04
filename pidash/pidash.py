# PiDash Project
# 2022 - Angelo Poggi angelo.poggi@enigmaconsulting.tech

from machine import Pin


class PiDash:
    def __init__(self):
        # want to init the pin at 0 value
        self.sen0105 = Pin(26, Pin.IN, Pin.PULL_DOWN)
        #init value to 0
        self.value = 0
        # self.sen0105.value = self.sen0105.read_digital()

    def increasespeed(self):
        return self.value + 1

    def decreasespeed(self):
        return self.value - 1



