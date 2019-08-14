from gpiozero import Servo, MCP3008
from time import sleep

pot = MCP3008(channel=0)
servo = Servo(21)

def map_values(x, a, b, c, d):
    """Maps value range from input to output."""
    y = (x-a)/(b-a) * (d-c)+c
    return y

while True:
    potReading = pot.value
    servoSetting = map_values(potReading, 0.0, 1.0, -1.0, 1.0)
    # Spew diagnostics to the terminal, but formatted neatly
    print("{0:1.3f}, {1:1.3f}".format(potReading, servoSetting))
    # Move the servo
    servo.value = servoSetting
    sleep(0.05)
