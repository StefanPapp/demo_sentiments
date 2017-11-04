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

print(api.VerifyCredentials())
statuses = api.GetUserTimeline(screen_name=user)
print([s.text for s in statuses])

users = api.GetFriends()

print([u.screen_name for u in users])
#print([u.name for u in users])
#print(api.GetSearch(raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100"))
#print(api.GetSearch(raw_query="q=from%3AStefanPapp%20%23FlinkForward&result_type=popular"))
print(api.GetSearch(raw_query="q=from%3Akyrah&result_type=recent&since=2014-07-19"))
