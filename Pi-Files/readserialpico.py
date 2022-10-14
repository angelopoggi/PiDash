#angelo.poggi@enigmaconsulting.tech
#Reads data over UART from Pico

from serial import Serial
import time

class ReadPicoSerial():
    def __init__(self):
        self.UART_COM = 'COM14'
        self.UART_BAUD = 9600
    def readpico(self):
        ser = Serial(self.UART_COM, self.UART_BAUD)
        time.sleep(1)
        while True:
            try:
                data = (ser.read(2))
                received_data = str(data, 'UTF-8')
                print(received_data)
            except KeyboardInterrupt:
                raise("KEYBOARD INTERUPT - OHMY!")