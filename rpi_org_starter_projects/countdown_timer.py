from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

green = (0,255,0)
red = (255,0,0)
black = (0,0,0)
s = 20

leds = []

for i in range(64):
    if i < s:
        leds.append(green)
    else:
        leds.append(black)

sense.set_pixels(leds)

sleep(5)

for i in range(s):
    leds[i] = red
    sense.set_pixels(leds)
    sleep(0.5)
    
for i in range(3):
    sense.clear()
    sleep(0.25)
    sense.set_pixels(leds)
    sleep(0.25)
    
sense.clear()