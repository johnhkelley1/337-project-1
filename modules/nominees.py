import settings
import util
import awards
def get(year):
	names = []
	tweets = []
	nominees = {}
	for award in settings.awards:
		nominees[award] = []
	x = 0
	for tweet in settings.data15:
		if x > 100000:
			break
		x += 1
		if 'nomin' in tweet['text']:
			tnames = util.names_from_text(tweet['text'])
			tawards = awards.awards_from_text(tweet['text'])
			for award in tawards:
				for name in tnames:
					if name.lower() not in award.lower():
						nominees[award].append(name)
	return nominees