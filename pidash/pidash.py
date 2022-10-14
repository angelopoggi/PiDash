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


import os
import utime
from machine import ADC

temp_sensor = ADC(4)  # Default connection of temperature sensor


def temperature():
    # get raw sensor data
    raw_sensor_data = temp_sensor.read_u16()

    # convert raw value to equivalent voltage
    sensor_voltage = (raw_sensor_data / 65535) * 3.3

    # convert voltage to temperature (celcius)
    temperature = 27 - (sensor_voltage - 0.706) / 0.001721

    return temperature


# print setup information :
print("OS Name : ", os.uname())

uart = machine.UART(0, baudrate=9600)
print("UART Info : ", uart)
utime.sleep(3)

while True:
    temp = int(temperature())
    print(str(temp))
    uart.write(str(temp))

    utime.sleep(1)
