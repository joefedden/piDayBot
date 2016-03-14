import tweepy, datetime, time

hour = datetime.datetime.now().time().hour
minutes = datetime.datetime.now().time().minute


currTime = str(hour) + ":" + str(minutes)
AMmessage = "It's Pi Time at " + str(currTime) + " AM!"
PMmessage = "It's Pi Time at 3:14 PM!"

CONSUMER_KEY = 'srGMSNKM3dv7isrpeJlHCEGYh'
CONSUMER_SECRET = 'RpwpXZpj6KAry9navg28iD1O9W2Hn7LOaB3D6iK9lG8aW4ytv0'
ACCESS_KEY = '709238984719740928-SxVlRmNYG0Bz3XkUHmNnT4XPrA77mtk'
ACCESS_SECRET = 'b6HAQih7xcgFOEVaO8WVAMthHQroboBukKH5FmzTOnCdK'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while(True):
	hour = datetime.datetime.now().time().hour
	minutes = datetime.datetime.now().time().minute
	AMmessage = "It's Pi Time at " + str(currTime) + " AM!"
	PMmessage = "It's Pi Time at 3:14 PM!"
	if (hour == 3 and minutes == 14):
		api.update_status(status=AMmessage)
		print("Posted at " + currTime)
	if (hour == 15 and minutes == 14):
		api.update_status(status=PMmessage)
		print("Posted at " + currTime)
	time.sleep(60)