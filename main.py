import utime
from machine import Pin,I2C,ADC,UART
from pico_i2c_lcd import I2cLcd

spdo = Pin(8, Pin.IN)
sda = Pin(4)
scl = Pin(5)
I2C_ADDR = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS =16
temp = ADC(4)
counter = 0
uart = UART(0,
            baudrate=9600,
            tx=Pin(0),
            rx=Pin(1),
            bits=8,
            parity=None,
            stop=1)

uart.init()

i2c = I2C(0,sda=sda,scl=scl,freq=400000)
lcd = I2cLcd(i2c,I2C_ADDR,I2C_NUM_ROWS,I2C_NUM_COLS)

def spdom(pin):
    global counter
    counter += 1

spdo.irq(trigger=Pin.IRQ_RISING, handler=spdom)

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
    #TEMPSHIT
    #this converts voltage
    conversion_factor = 3.3 / (65535)
    reading = temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    temperature = temperature * 2 + 30
    temperature = int(temperature)
    #SERIAL SHIT
    message = str(temperature) + '\n'
    uart.write(bytes(message, 'utf-8'))