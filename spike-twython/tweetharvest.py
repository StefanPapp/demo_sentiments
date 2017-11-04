#!/bin/python
 
# Load twython library
import json  # Teach python JSON
from twython import Twython, TwythonError, TwythonStreamer # Load libraries for twitter API
import pymongo # Teach python to talk to MongoDB
 
# Setup Authentificaion Settings
APP_KEY = 'xlppp5yvBuQfMYOIi8JsKDrNc' # Consumer key
APP_SECRET = 'lO7y6WvCBCTXKMZujRp4fy9z7fserzfa2aSObxl6FsGaWcsYaz' # Consumer secret
 
OAUTH_TOKEN = '14316485-1LcHNfLCqTUHJ5oreG9rVbxmbqcaSjFcim20Axmnh'  # Access token
OAUTH_TOKEN_SECRET = 'ZIZWaMj0G16EMZ4DxRqoZZkD09gpKgjvS3GFoR9HTuxPD'  # Access tocen secret
 

# Obtain an OAuth 2 Access Token
twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
 
# Use the Access Token
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
 
# Setup a connection to mongodb
#connection = pymongo.Connection('localhost', 27017)
#db = connection.twitter
 
# Define a class to handle the stream
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data)
            # db.tweets.save(data) # Take the data in text and save it to the mongodb twitter.tweets
 
    def on_error(self, status_code, data):
        print status_code, data
 
# Start the stream
# Requires Authentication as of Twitter API v1.1
stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
 
stream.statuses.filter(locations = '-74,40,-73,41')