from gpiozero import LED
from time import sleep

# LED connected to GPIO pin 25
led = LED(25)

led.on()
sleep(0.5)
led.off()
sleep(0.5)
led.on()
sleep(1)
led.off()

led.close()