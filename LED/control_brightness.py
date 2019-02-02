from gpiozero import PWMLED, MCP3008
from time import sleep

# the potentiometer is connected to the ADC chip (MCP3008) via channel 0 (is pin 1 on the chip)
# via this channel the potentiometer will input an analog signal to the chip
pot = MCP3008(0)

# the red LED is connected to the rapsberry pi via GPIO pin 17
# the blue LED is connected to the rapsberry pi via GPIO pin 18
# with the PWMLED object we can apply Pulse-Width Modulation (PWM)
# PWM translates the analog signal of the potentiometer into digital pulses to the LED
# the more distance (or duty cycle) between the pulses, the lower the brightness of the LED
led_red = PWMLED(17)
led_blue = PWMLED(18)


while True:
    if pot.value < 0.001:
        led_red.value = 0
        led_blue.value = 0
    else:
        led_red.value = pot.value

        # blue LED starts lighting up after pot.value > 0.5
        if pot.value > 0.5:
            led_blue.value = pot.value

        print(pot.value)
        sleep(0.1)