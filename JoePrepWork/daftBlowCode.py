import explorerhat
from time import sleep

#spin the first and second motor at 100% forward

explorerhat.motor.one.forward()
explorerhat.motor.two.forward()

sleep(100)
