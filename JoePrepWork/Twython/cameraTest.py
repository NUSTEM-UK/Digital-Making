# take a photo and add a border script
from picamera import PiCamera
from time import sleep

camera = PiCamera()

def snap():
    camera.start_preview()
    camera.image_effect = 'posterise'
    sleep(5)
    camera.capture('camImage.jpg')
    camera.stop_preview()

if __name__ == "__main__":
    snap()