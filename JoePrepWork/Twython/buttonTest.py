# button to action code
# mainly robbed from https://gpiozero.readthedocs.io/en/stable/recipes.html#button-controlled-camera

from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause

button = Button(3)
camera = PiCamera()

def capture():
    print("Snap")
    timestamp = datetime.now().isoformat()
    camera.capture('%s.jpg' % timestamp)

button.when_pressed = capture

pause()