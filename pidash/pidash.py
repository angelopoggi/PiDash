#PiDash Project
#2022 - Angelo Poggi angelo.poggi@enigmaconsulting.tech

from machine import Pin

class PiDash:
    def __init__(self):
        #want to init the pin at 0 value
        self.sen0105 = Pin(26, Pin.IN, Pin.PULL_DOWN)
        #self.sen0105.value = self.sen0105.read_digital()
    def pulsegenread(self):
        #starting off at Zero
        speed_increment = 0
        vehicle_speed = 0
        while True:
            if self.sen0105.value() == 1:
                speed_increment += 1
                if speed_increment == 16000:
                    vehicle_speed += 1
                    # reset speed and start over
                    speed_increment == 0
            elif self.sen0105.value() == 0:
                # if we get no pulse start subtracting
                speed_increment -= 1
                if speed_increment == 0:
                    vehicle_speed -= 1
            print(vehicle_speed)



