from time import sleep
from envirophat import light, motion

while True:
    rgb = light.rgb()
    heading = motion.heading()
    
    print(rgb, heading)
    sleep(0.2)
