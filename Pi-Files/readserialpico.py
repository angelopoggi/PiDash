#angelo.poggi@enigmaconsulting.tech
#Reads data over UART from Pico

from serial import Serial, PARITY_NONE, STOPBITS_ONE, EIGHTBITS
import time

class ReadPicoSerial():
    def __init__(self):
        self.UART_COM = '/dev/ttyAMA0'
        self.UART_BAUD = 9600

    def readpico(self):
        ser = Serial(self.UART_COM,
                     self.UART_BAUD,
                     parity=PARITY_NONE,
                     stopbits=STOPBITS_ONE,
                     bytesize=EIGHTBITS,
                     timeout=1000
                     )
        while True:
            try:
                data = ser.read(2048)
                print(data)
            except KeyboardInterrupt:
                raise("KEYBOARD INTERUPT - OHMY!")