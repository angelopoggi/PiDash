# PiDash
---

PiDash aims to provide a digital dashboard for older vehicles.
Development is based on a 1972 Mercedes 220D. Collaboration for different
sensors and vehicles is appreciated

# Hardware used for testing

Board: Raspberry Pi Pico
Speedometer Sending Unit: Dakota-Digital SEN-01-05 16K PPM

# Change logs

## 2022 05 04

After some more research, it just turns out this is just a hall sensor.
So far, I am just testing in main.py, but the idea will be that during an interupt on Rising,
we know that the speedometer is spinning. We should count 16,0000 of these and do the inverse to reduce speed.
I still havent wrapped my head around the flow for that.

[Helpful video that got me on the path](https://www.youtube.com/watch?v=JjkeCPV8h38)


```
```