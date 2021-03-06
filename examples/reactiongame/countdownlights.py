import explorerhat
from time import sleep
import random

def countdown():
    #turn on all the lights on the explorerHat
    explorerhat.light.yellow.on()
    explorerhat.light.blue.on()
    explorerhat.light.red.on()
    explorerhat.light.green.off()

    #then turn them off, but with a random delay between each light for added tension / fun
    sleep(random.uniform(1,5))
    explorerhat.light.blue.off()

    sleep(random.uniform(1,5))
    explorerhat.light.yellow.off()

    sleep(random.uniform(1,5))
    explorerhat.light.red.off()
    explorerhat.light.green.on()

countdown()

# Now clean up after ourselves
sleep(3)
explorerhat.explorerhat_exit()