#angelo.poggi@enigmaconsulting.tech
#Reads data over UART from Pico

from serial import Serial, PARITY_NONE, STOPBITS_ONE, EIGHTBITS
import time
import binascii

class ReadPicoSerial():
    def __init__(self):
        self.UART_COM = '/dev/serial0'
        self.UART_BAUD = 9600

    def readpico(self):
        ser = Serial(self.UART_COM,
                     self.UART_BAUD,
                     parity=PARITY_NONE,
                     stopbits=STOPBITS_ONE,
                     bytesize=EIGHTBITS,
                     timeout=0
                     )
        while True:
            try:
                data = ser.read(100)
                try:
                    converted_data = int(data, 16)
                    print(converted_data)
                except:
                    print(0)

                #convert it to a readable format
                #converted_data = int(data, 16)
                #print(converted_data)
                time.sleep(1)
                # received_data = str(data, 'UTF-8')
                # print(received_data)
            except KeyboardInterrupt:
                raise("KEYBOARD INTERUPT - OHMY!")