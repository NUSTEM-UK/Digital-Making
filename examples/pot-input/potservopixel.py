from gpiozero import Servo, MCP3008
import board
import neopixel
from time import sleep
from colorwheel import wheel

# Set up potentiometer
pot = MCP3008(channel=0)

# Set up servo
servo = Servo(21)

# Set up NeoPixel
pixel_pin = board.D18
num_pixels = 1

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2)


def map_values(x, a, b, c, d):
    """Maps value range from input to output."""
    y = (x-a)/(b-a) * (d-c)+c
    return y

while True:
    potReading = pot.value
    servoSetting = map_values(potReading, 0.0, 1.0, -1.0, 1.0)
    
    ########
    # Calculate hue here
    ########

    # Spew diagnostics to the terminal, but formatted neatly
    print("{0:1.3f}, {1:1.3f}, {2:3d}".format(potReading, servoSetting, hue))
    # Move the servo
    servo.value = servoSetting
    
    ########
    # Set the LED colour here
    ########

    sleep(0.05)
