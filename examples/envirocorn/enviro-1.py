from time import sleep
from envirohat import light, motion

rgb = light.rgb()
haeding = motion.heading()

while True:
    print(rgb)
    print(heading)
    sleep(0.1)
