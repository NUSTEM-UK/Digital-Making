from blinkt import set_pixel, set_brightness, show, clear
from gpiozero import DigitalInputDevice

set_brightness(0.1)

# My function takes three values of 0 or 1 and sets the NeoPixels
def theFloorShow(r,g,b):
    for pixel in range(8):
        set_pixel(pixel,r*255,g*255,b*255)
        show()

# I need 3 switches - red, blue and green that give 0/1 (on or off) for each colour
# https://gpiozero.readthedocs.io/en/stable/api_input.html#base-classes

# GPIO pins have physical pull_up resistors so set to True, use pins 2,3 and reserve 4 for the green switch
blueB = DigitalInputDevice(2, pull_up=True)
redB = DigitalInputDevice(3, pull_up=True)

# My loop
while True:
    # I've not the the green toggle switch wired up yet so I'll input a value of 0 for green
    theFloorShow(redB.value, 0, blueB.value)
