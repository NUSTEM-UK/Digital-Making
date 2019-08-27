import explorerhat
from time import sleep

#spin the first and second motor at 100% forward
explorerhat.motor.one.forward()
explorerhat.motor.two.forward()

#leave it running for 5 seconds
sleep(5)

#turn the motors off
explorerhat.motor.one.forward(0)
explorerhat.motor.two.forward(0)