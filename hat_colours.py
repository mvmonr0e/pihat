#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

yellow = (0,255,255)
blue = (255,0,255)
speed = 0.05
message = "Hello World!"

sense.show_message(message,speed,text_colour=yellow,back_colour=blue)

sense.clear()
