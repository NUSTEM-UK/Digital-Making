import explorerhat
from time import sleep
import random

#turn on all the lights on the explorerHat
explorerhat.light.yellow.on()
explorerhat.light.blue.on()
explorerhat.light.red.on()

#then turn them off, but with a random delay between each light for added tension / fun
explorerhat.light.green.off()
sleep(random.randint(1,20)/10)
explorerhat.light.blue.off()
sleep(random.randint(1,20)/10)
explorerhat.light.yellow.off()
sleep(random.randint(1,20)/10)
explorerhat.light.red.off()
explorerhat.light.green.on()