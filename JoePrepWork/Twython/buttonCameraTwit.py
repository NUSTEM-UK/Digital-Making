# Button press, take photo, publish to Twitter code 1.0

# Import Twython and our Twitter credentials
from twython import Twython
from twythonCreds import *

# import timestamper
from datetime import datetime

# Import our the camera module
from picamera import PiCamera
from time import sleep

# import GPIOzero for the Button
from gpiozero import Button
from signal import pause

# I need to change the satus each time so I don't get blocked from Twitter
import random

#initiate Twitter
twitter = Twython (APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# initiate the Button
button = Button(3)

# initiate the Camera
camera = PiCamera()

# Media Upload Function
def mediaUp():
	photo = open('camImage.jpg', 'rb')
	response = twitter.upload_media(media=photo)
	ranNum = str(random.randint(1,101))
	twitter.update_status(status=ranNum, media_ids=[response['media_id']])
	print("Twitter image uploaded successfully")
	photo.close()
	
# Picture taker
def snapSnap():
	camera.capture('camImage.jpg')
	print("Snap")
	mediaUp()
		
if __name__ == "__main__": 
	button.when_pressed = snapSnap
	pause()
