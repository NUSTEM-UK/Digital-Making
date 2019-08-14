import explorerhat
from time import sleep
import random

def countdown():
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

    #then set the trigger to allow button presses
    trigger = True
    
    return trigger

trigger = countdown()

if trigger:
    

while True:
    for i in range(100):
        explorerhat.motor.one.forward(i)
        sleep(0.1)

