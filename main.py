import sys

from pidash.pidash import PiDash
from machine import Pin
#using absolute path here to import for testing

dashinit = PiDash()

value = 0

def increasespeed(value):
    return value + 1


def decreasespeed(value):
    return value - 1

dashinit.sen0105.irq(trigger=Pin.IRQ_RISING, handler=dashinit.increasespeed())
dashinit.sen0105.irq(trigger=Pin.IRQ_FALLING, handler=dashinit.decreasespeed())

try:
    while True:
        print(dashinit.value)
except:
    sys.exit()