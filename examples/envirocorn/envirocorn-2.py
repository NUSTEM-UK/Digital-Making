from time import sleep
from envirophat import light, motion
import unicornhathd

unicornhathd.brightness(1.0)
unicornhathd.clear()
unicorn_height = unicorn_width = 16

bar_speed = 1
bar_width = 1

def map_values(x, a, b, c, d):
    """Maps value range from input to output."""
    y = (x-a)/(b-a) * (d-c)+c
    return y

# Make ourselves an empty array
values_y = [None] * 16

while True:
    # We need separate RGB values for the UnicornHAT
    r, g, b = light.rgb()
    heading = motion.heading()

    # Drop the first height value from the list
    values_y.pop[0]
    # Add a value to the end, calculated from the heading
    values_y.append(map_values(heading, 0, 359, 0, 15))

    for x in range(16):
        for y in range (values_y[x]):
            unicornhathd.set_pixel(x, y, r, g, b)
        
    print(r, g, b, heading, brightness)

    unicornhathd.show()

    sleep(1.0 / bar_speed)
