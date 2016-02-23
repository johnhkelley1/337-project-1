import settings
import util
import awards
import re
import sys
def get(year):
	names = []
	tweets = []
	nominees = {}
	for award in settings.awards:
		nominees[award['name']] = {}
	data = []
	if year == '2015':
		data = settings.data15
	else:
		data = settings.data13
	x = 0

	for tweet in data:
		if x % 5000 == 0:
			sys.stdout.write(" Progress: %s/%s \r" % (x, len(data)))
			sys.stdout.flush()

		x += 1
		#if 'nomin' in tweet['text']:
		for award in settings.awards:
			matched = False
			for regex in award['regexs']:
				if re.search(regex, tweet['text'], re.IGNORECASE):
					matched = True
					break

			if matched:
				if award['type'] == 0:
					tnames = util.get_movie_names(tweet['text'])
				else:
					tnames = util.get_human_names(tweet['text'])
				for name in tnames:
					if name.lower() not in award['name'].lower():
						if name in nominees[award['name']]:
							nominees[award['name']][name] += 1
						else:
							nominees[award['name']][name] = 1
					#tawards = awards.awards_from_text(tweet['text'])
					'''
			for award in tawards:
				for name in tnames:
					if name.lower() not in award.lower():
						if name in nominees[award]:
							nominees[award][name] += 1
						else:
							nominees[award][name] = 1
							'''

	nominees2 = {}
	for award in nominees:
		nominees2[award] = []
		for key,val in nominees[award].iteritems():
			nominees2[award].append({"name":key,"count":val})
		nominees2[award].sort(key=lambda x: -1*x['count'])
		nominees2[award] = [p['name'] for p in nominees2[award][:20]]

	return nominees2
