from gpiozero import LED
from time import sleep

# LED connected to GPIO pin 25
led = LED(25)

# sleep time
delay = 1

while True:
    led.on()
    sleep(delay)
    led.off()
    sleep(delay)