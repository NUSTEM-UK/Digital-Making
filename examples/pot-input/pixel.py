"""Test NeoPixel strip attached to pin 18.

Run with sudo (required for hardware access in this case)

Dependencies (pip3 install):
    RPI.GPIO
    adafruit-blinka
    rpi_ws281x
"""

import board
import neopixel
from time import sleep
from colorwheel import wheel

pixel_pin = board.D18
num_pixels = 1

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2)


# Setup complete. Let's display some colours!

# Red!
pixels.fill((255, 0, 0))
sleep(1)
# Green!
pixels.fill((0, 255, 0))
sleep(1)
# Blue!
pixels.fill((0, 0, 255))
sleep(1)

# Now let's cycle around all the colours, using a hue angle
# calculation care of wheel()

for hue in range(255):
    pixels.fill(wheel(hue))
    sleep(0.02) # Pause briefly for us to coo at the pretty light

# Pause for a second
sleep(1)

# Finally, turn the pixels off:
pixels.fill((0, 0, 0))
