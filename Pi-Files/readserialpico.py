#angelo.poggi@enigmaconsulting.tech
#Reads data over UART from Pico

import serial
import time

class ReadSerial():
    def __init__(self):
        self.UART_COM = 'COM14'
        self.UART_BAUD = 9600
    def readserial(self):
        ser = serial.Serial(self.UART_COM, self.UART_BAUD)
        time.sleep(1)
        while True:
            data = (ser.read(2))
            received_data = str(data, 'UTF-8')
            print(received_data)










