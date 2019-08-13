from time import sleep
from envirophat import light, motion
import unicornhathd

unicornhathd.brightness(1.0)
unicornhathd.clear()

def map_values(x, a, b, c, d):
    """Maps value range from input to output."""
    y = (x-a)/(b-a) * (d-c)+c
    return y

while True:
    # We need separate RGB values for the UnicornHAT
    r, g, b = light.rgb()
    heading = motion.heading()
    # Heading is 0-359 degrees; map to 0-1.0 for UnicornHAT brightness
    brightness = map_values(heading, 0, 359, 0.0, 1.0)
    
    print(r, g, b, heading, brightness)

    unicornhathd.set_all(r, g, b)
    unicornhathd.brightness(brightness)
    unicornhathd.show()

    sleep(0.1)
