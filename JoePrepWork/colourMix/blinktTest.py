from blinkt import set_pixel, set_brightness, show, clear
import time
from gpiozero import DigitalInputDevice

set_brightness(0.1)

while True:
    for i in range(8):
        clear()
        set_pixel(i, 255, 0, 0)
        show()
        time.sleep(0.5)


# I need 3 switches - blue, red and green
# that give 0/1 for colour
https://gpiozero.readthedocs.io/en/stable/api_input.html#base-classes

blueB = DigitalInputDevice(2)
redB = DigitalInputDevice(3)
yellowB = DigitalInputDevice(4)

# to go in loop
blueVal = blueB.value