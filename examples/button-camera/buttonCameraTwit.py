# Button press, take photo, publish to Twitter code 1.0

### Things to try #######################################################################
#   Change the status message to something a little more interesting                    #
#   than a random number                                                                #
#                                                                                       #
#   Add a cool filter to the photo to impress your followers - check link for ideas     #
#   https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/8        #
#                                                                                       #
#########################################################################################


# Import Twython and our Twitter credentials
from twython import Twython
from twythonCreds import *

# Import our the camera module
from picamera import PiCamera

# import GPIOzero for the Button
from gpiozero import Button
from signal import pause

# I need to change the status each time so I don't get blocked from Twitter
import random

#initiate Twitter, Button and the PiCamera
twitter = Twython (APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
button = Button(3)
camera = PiCamera()

# add your camera filters and annotations in here

randomStatuses = ("What a great face I have!", "Look at me, look at me!", "S'up", "This is my face!")

# Picture taker
def snapSnap():
    camera.capture('camImage.jpg')
    print("Snap")
    tweetImage()

# Media Upload Function
def tweetImage():
    photo = open('camImage.jpg', 'rb')
    response = twitter.upload_media(media=photo)
    ranNum = random.randint(0,len(randomStatuses)-1)
    twitter.update_status(status=randomStatuses[ranNum], media_ids=[response['media_id']])
    print("Twitter image uploaded successfully")
    photo.close()
        
if __name__ == "__main__": 
    button.when_pressed = snapSnap
    pause()