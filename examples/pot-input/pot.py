from gpiozero import MCP3008
from time import sleep

pot = MCP3008(channel=0)

while True:
    print(pot.value) # Will be a floating point number between 0 and 1
    sleep(0.25)
