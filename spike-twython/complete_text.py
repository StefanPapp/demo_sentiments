#!/usr/bin/env python

from twython import Twython

APP_KEY = "xlppp5yvBuQfMYOIi8JsKDrNc"
APP_SECRET = "lO7y6WvCBCTXKMZujRp4fy9z7fserzfa2aSObxl6FsGaWcsYaz"
atk = "14316485-1LcHNfLCqTUHJ5oreG9rVbxmbqcaSjFcim20Axmnh"
ats = "ZIZWaMj0G16EMZ4DxRqoZZkD09gpKgjvS3GFoR9HTuxPD"
user = "StefanPapp"
# Twython(APP_KEY, access_token=ACCESS_TOKEN)
twitter = Twython(APP_KEY, APP_SECRET, atk, ats)
twitter.verify_credentials()
results = twitter.cursor(twitter.search, q='python')
for result in results:
    print result