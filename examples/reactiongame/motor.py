import explorerhat
from time import sleep

#spin the first and second motor at 100% forward
explorerhat.motor.one.forward()
explorerhat.motor.two.forward()

#leave it running for 5 seconds
sleep(5)

# Now clean up after ourselves
explorerhat.explorerhat_exit()