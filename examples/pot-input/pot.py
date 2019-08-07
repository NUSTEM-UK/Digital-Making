from gpiozero import MCP3008
from time import sleep

# We're going to connect a potentiometer to pin 0 on the MCP3008
pot = MCP3008(channel=0)

# Now just read the value and spit it out. Again and again.
while True:
    print(pot.value) # Will be a floating point number between 0 and 1
    sleep(0.25)
