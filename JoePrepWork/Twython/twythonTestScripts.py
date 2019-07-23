# Twython test code: Publishing Statuses and Images
# import Twython and Credentials
from twython import Twython
from twythonCreds import *

# test code for timestamps on tweets
from datetime import datetime

# current date and time
now = datetime.now()
timestamp = str(datetime.fromtimestamp(datetime.timestamp(now)))
print("timestamp =", timestamp)

# Create Twython instance using credentials from twythonCreds
twitter = Twython (APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Update test status
twitter.update_status(status = timestamp)