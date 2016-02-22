import settings
import util
import awards
import re
def get(year):
	names = []
	tweets = []
	nominees = {}
	for award in settings.awards:
		nominees[award['name']] = {}
	x = 0
	for tweet in settings.data15:
		# if x > 100000:
		# 	break
		if x % 100000 == 0:
			print "%s/%s" % (x, len(settings.data15))
		x += 1
		#if 'nomin' in tweet['text']:
		for award in settings.awards:
			matched = False
			for regex in award['regexs']:
				if re.search(regex, tweet['text'], re.IGNORECASE):
					matched = True
					break

			if matched:
				# if award['type'] == 0:
				tnames = util.names_from_text(tweet['text'])
				# else:
				# 	tnames = util.get_human_names(tweet['text'])
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
		#nominees2[award] = [p['name'] for p in nominees2[award][:10]]
		if len(nominees2[award]) > 0:
			nominees2[award] = nominees2[award][0]['name']
		else:
			nominees2[award] = ""

	return nominees2