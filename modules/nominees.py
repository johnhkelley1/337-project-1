import settings
import util
def get(year):
	names = []
	tweets = []
	x = 0
	for tweet in settings.data15:
		if x > 5000:
			break
		x += 1
		if 'nomin' in tweet['text']:
			tnames = util.names_from_text(tweet['text'])
			for name in tnames:
				names.append(name)
				tweets.append(tweet['text'])
	return tweets