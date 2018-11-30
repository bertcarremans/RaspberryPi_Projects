# Source: https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat

from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

green = (0, 255, 0) 
red = (255, 0, 0)
yellow = (247, 252, 185)
scroll_speed = 1.0

# ----------------
# Show a message
# ----------------
'''
sense.show_message("mona"
                   , scroll_speed=scroll_speed
                   , text_colour=green)
'''

# ----------------
# Show letters
# ----------------

letters = ['a','s','z','t','d','m','l','h','e','n']


def pick_random_colour():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    colour = (r, g, b)
    return colour
    
# show_letter does only allow one letter
for l in range(len(letters)):
    print(letters[l])
    #sense.show_letter(letters[l], pick_random_colour())
    sense.show_letter(str(randint(0,10)))
    sleep(5)


# ----------------
# Color pixels
# ----------------
'''
B = (102, 51, 0)
b = (0, 0, 255)
S = (205,133,63)
W = (255, 255, 255)

# Set up where each colour will display
steve_pixels = [
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, S, S, S, S, S, S, B,
    S, S, S, S, S, S, S, S,
    S, W, b, S, S, b, W, S,
    S, S, S, B, B, S, S, S,
    S, S, B, S, S, B, S, S,
    S, S, B, B, B, B, S, S
]

# Display these colours on the LED matrix
sense.set_pixels(steve_pixels)
sleep(5)

# ----------------
# Setting rotation
# ----------------
sense.flip_v()
sleep(5)
'''

# -------------------------
# Temp, humidity, pressure
# -------------------------
'''
temp = round(sense.get_temperature(),1)
temp_h = round(sense.get_temperature_from_humidity(),1)
temp_p = round(sense.get_temperature_from_pressure(),1)
print('temp shorthand humidity',temp)
print('temp humidity',temp_h)
print('temp pressure',temp_p)

humid = round(sense.get_humidity(),1)
press = round(sense.get_pressure(),1)
print('humidity', humid)
print('pressure', press)

thp = 'Temperature: ' + str(temp) + ' Humidity: ' + str(humid) + ' Pressure: ' + str(press)

# Check if measurements are wihtin normal ranges
if temp > 18.3 and temp < 26.7:
    back_colour = green
else:
    back_colour = red
    
sense.show_message(thp
                   , scroll_speed=scroll_speed
                   , back_colour=back_colour)
'''    
    
# -------------------------
# Pitch, roll, yawn
# -------------------------
'''
o = sense.get_orientation()
pitch = o['pitch']
roll = o['roll']
yaw = o['yaw']
print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
'''

# -------------------------
# X, Y, Z
# -------------------------
'''
sense.show_letter('J')
while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    # Detecting change of gravitational force on axes
    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)
    
    if x == -1:
        sense.set_rotation(180)
    elif y == 1:
        sense.set_rotation(90)
    elif y == -1:
        sense.set_rotation(270)
    else: 
        sense.set_rotation(0)
    
    print("x={0}, y={1}, z={2}".format(x, y, z))
    
    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1 or y > 1 or z > 1:
        sense.show_letter("!", red)
    else:
        sense.clear()
'''
    
# -------------------------
# Joystick
# ------------------------- 
'''
while True:
    for event in sense.stick.get_events():
        #print(event.direction, event.action)
        d = event.direction
        sense.show_letter(d[0].upper())
        sleep(0.5)
        sense.clear()
'''
























sense.clear()

