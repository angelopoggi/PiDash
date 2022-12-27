import utime
from machine import Pin,ADC,UART

spdo = Pin(8, Pin.IN)
temp = ADC(4)
counter = 0
uart = UART(0)
tire_diameter = 27.9
tire_circumference = tire_diameter * 3.1416

uart.init(9600)


'''
NEED THE FOLLOWING SENDING UNITES
1. Water/Coolant
3. Oil Pressure

For fuel tank we will use ADC to use the exsisting sending unit
'''

def spdom(pin):
    global counter
    counter += 1
def calc_speed(rpm, tire_circumference):
    speed = rpm * tire_circumference / 5280 * 12
    #returns the speed rounded to the nearest whole number
    return round(speed)
def calc_temp():
    conversion_factor = 3.3 / (65535)
    reading = temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    temperature = temperature * 2 + 30
    temperature = int(temperature)
    return temperature

spdo.irq(trigger=Pin.IRQ_RISING, handler=spdom)

while True:
    utime.sleep(1)
    rpst =  counter // 16
    rps = rpst // 1
    rpm = rps * 60
    speed = calc_speed(rpm, tire_circumference)
    print(speed)
    uart.write(speed)
    counter = 0