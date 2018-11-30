from sense_hat import SenseHat
import time
from PIL import Image
import os

# Open image file
image_file = os.path.join(os.sep,"/home","pi","Desktop","sense_hat","bb8.png")
img = Image.open(image_file)


# Generate rgb values for image pixels
rgb_img = img.convert('RGB')
image_pixels = list(rgb_img.getdata())


# Get the 64 pixels you need
pixel_width = 6
image_width = pixel_width*8
sense_pixels = []
start_pixel = 0
while start_pixel < (image_width*64):
    sense_pixels.extend(image_pixels[start_pixel:(
start_pixel+image_width):pixel_width])
    start_pixel += (image_width*pixel_width)

# Display the image
sense = SenseHat()
sense.set_rotation(r=180)
sense.set_pixels(sense_pixels)
time.sleep (10)

sense.clear()

