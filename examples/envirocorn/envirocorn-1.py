from time import sleep
from envirophat import light, motion
import unicornhathd

unicornhathd.brightness(0.5)
unicornhathd.clear()

def map_values(x, a, b, c, d):
    """Maps value range from input to output."""
    y = (x-a)/(b-a) * (d-c)+c
    return y

while True:
    rgb = light.rgb()
    heading = motion.heading()
    
    print(rgb, heading)

    unicornhathd.set_all(rgb)
    unicornhathd.brightness(heading, 0, 359, 0.0, 1.0)
    unicornhathd.show()

    sleep(0.2)
