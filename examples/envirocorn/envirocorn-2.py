from time import sleep
from envirophat import light, motion
import unicornhathd

unicornhathd.brightness(1.0)
unicornhathd.clear()
unicorn_height = unicorn_width = 16

bar_speed = 12
bar_width = 1

def map_values(x, a, b, c, d):
    """Maps value range from input to output."""
    y = (x-a)/(b-a) * (d-c)+c
    return y

# Make ourselves an empty array
values_y = [int(0)] * 16

while True:
    # We need separate RGB values for the UnicornHAT
    r, g, b = light.rgb()
    heading = motion.heading()

    # Drop the first height value from the list
    values_y.pop(0)
    # Add a value to the end, calculated from the heading
    values_y.append(int(map_values(heading, 0, 359, 0, 16)))

    for x in range(16):
        for y in range(16):
            this_brightness = min(1, values_y[x]-y)
            if this_brightness > 0:
                mult = 1
            else:
                mult = 0
            unicornhathd.set_pixel(x, y, r*mult, g*mult, b*mult)
        
    print(r, g, b, heading)

    unicornhathd.show()

    sleep(1.0 / bar_speed)
