from gpiozero import Servo
from time import sleep

servo = Servo(21)

while True:
    servo.value = -1.0
    sleep(1)
    servo.value = 0.0
    sleep(1)
    servo.value = 1.0
    sleep(1)

