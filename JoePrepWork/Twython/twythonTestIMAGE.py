# Twython test code: Publishing Statuses and Images
# import Twython and Credentials
from twython import Twython
from twythonCreds import *
from cameraTest import *

# test code for timestamps on tweets
from datetime import datetime

# current date and time
now = datetime.now()
timestamp = str(datetime.fromtimestamp(datetime.timestamp(now)))
print("timestamp =", timestamp)

# Create Twython instance using credentials from twythonCreds
twitter = Twython (APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# open the test image
# photo = open('test.jpeg', 'rb')
# print("Photo opened successfully")

#take the picture
snap()
print("Photo taken")

photo = open('camImage.jpg', 'rb')
print("Photo opened successfully")

response = twitter.upload_media(media=photo)
print("Response created successfully")

twitter.update_status(status=timestamp, media_ids=[response['media_id']])
print("Twitter image uploaded successfully")