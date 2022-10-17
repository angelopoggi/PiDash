import utime
from machine import Pin,ADC,UART

spdo = Pin(8, Pin.IN)
temp = ADC(4)
counter = 0
uart = UART(0,9600)

uart.init()

def spdom(pin):
    global counter
    counter += 1

spdo.irq(trigger=Pin.IRQ_RISING, handler=spdom)

def genpayload(speed, temp):
    dict =  {
        'speed' : speed,
        'temp' : temp
    }
    return str(dict)

while True:
    utime.sleep(1)
    #SPEEDSHIT
    rpst =  counter / 16
    rps = rpst / 1
    rpm = rps * 60
    td = 14 * 3.1416
    vel = rpm * td
    vel = vel // 2.8
    vel = vel / 16000
    vel  = int(vel)
    # #TEMPSHIT
    # #this converts voltage
    conversion_factor = 3.3 / (65535)
    reading = temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    temperature = temperature * 2 + 30
    temperature = int(temperature)
    #SERIAL SHIT
    payload = genpayload(vel, temperature) + '\n'
    uart.write(str(payload))