import twitter

api_key = "xlppp5yvBuQfMYOIi8JsKDrNc"
api_secret = "lO7y6WvCBCTXKMZujRp4fy9z7fserzfa2aSObxl6FsGaWcsYaz"
atk = "14316485-1LcHNfLCqTUHJ5oreG9rVbxmbqcaSjFcim20Axmnh"
ats = "ZIZWaMj0G16EMZ4DxRqoZZkD09gpKgjvS3GFoR9HTuxPD"
user = "StefanPapp"
api = twitter.Api(consumer_key=api_key,
                      consumer_secret=api_secret,
                      access_token_key=atk,
                      access_token_secret=ats)

username = "StefanPapp"
querystring = "q=from%3A" + username+ "&result_type=recent&since=2014-07-19"
print(api.GetSearch(raw_query=querystring))
