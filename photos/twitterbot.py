import tweepy,time, sys
from django.conf import settings


#find better way for import

#settings.configure()
print settings.DEBUG
auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_KEY, settings.ACCESS_SECRET)
api = tweepy.API(auth)

#api.update_status("@Ne_parkiraj_tu Yo yo yo!")
#print dir(api.mentions_timeline()[0])
#print dir(api.mentions_timeline()[0].author)
#for mention in api.mentions_timeline():
#	print mention.author.screen_name, mention.text

def debug_print(text):
    """Print text if debugging mode is on"""
    # if settings.debug:
    #     print text
    if True:
    	print text

def imagecheck(tweet):
	"""Checks if tweet contains an image (of improperly parked car)"""
	pass

def get_last_id(filename):
	
	with open(filename) as f:
		last_id = int(f.read())
		return last_id

def save_new_id(filename,new_id):
	last_id = get_last_id(filename)

	if last_id<new_id:
		with open(filename, 'w') as f:
			f.write(str(new_id))
	else:
		debug_print('Recived smaller ID, not saving. Old: %d, New: %s'
					% (last_id,new_id))

def get_new_mentions():
	return api.mentions_timeline(since_id=get_last_id("last_id"))

def retweet_new_mentions():
	new_mentions = get_new_mentions().reverse()
	#if there is new mentions save the latest id
	if new_mentions:
		save_new_id("last_id",new_mentions[-1].id)
	else:
		return
	for mention in new_mentions:
		#check if tweet is "valid"
		rt_if_valid(mention)
		
def rt_if_valid(tweet):
	"""Retweet only if tweet/mention is valid a.k.a contains an image"""
	api.retweet(id=tweet.id)
#Create thread which will check for the latest mentions.
#Save the last retweed tweet id in some file so it will
#know what tweets are new.
#Parse text so everything except @Username will bi descrption 
#in new Post object.
#Also monitor for tweets with certain hashtag. I guess second thread
#for that will be needed.
#What if user mention bot account and put wanted hashtag?
#"mention" thread should disregard every hashtag (including #neparkiraju)
#and "hashtag" thread should dsregard tweets with @Ne_parkiraj_tu username

if __name__ == "__main__":
	#print get_last_id("last_id")
	#save_new_id("last_id", 0)
	#print get_last_id("last_id")
	#mentions = get_new_mentions()
	#pristupi fotki 
	#print "novi tvitovi", mentions[0].entities['media']['sizes']
    print "printaj"
    print settings.ACCESS_KEY
	