# Import our the camera module
from picamera import PiCamera
from time import sleep

# Initiate the PiCamera
camera = PiCamera()

# add an image effect - you can find more here: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/8
camera.image_effect = 'posterise'

# add a caption
camera.annotate_text = "Best photo ever!" 

# start the camera preview window
camera.start_preview()

# wait for two seconds
sleep(2)

# take picture
camera.capture('camImage.jpg')

# close the preview window
camera.stop_preview()