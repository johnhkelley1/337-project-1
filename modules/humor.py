import settings
import sys
from copy import deepcopy

def get(year):
    data = []
    if year == '2015':
        data = settings.data15
    else:
        data = settings.data13
    joke_freq = {}
    x = 0
    for tweet in data:
        x+=1
        if x % 5000 == 0:
			sys.stdout.write(" Progress: %s/%s \r" % (x, len(data)))
			sys.stdout.flush()
        if 'joke' in tweet['text']:
            if tweet['text'] in joke_freq:
                joke_freq[tweet['text']] += 1
            else:
                joke_freq[tweet['text']] = 1

    for key,val in deepcopy(joke_freq).iteritems():
        if val == 1:
            del joke_freq[key]


    jokes = [(key, val) for key, val in joke_freq.iteritems()]
    jokes.sort(key=lambda x: x[1]*-1)
    return [joke[0] for joke in jokes[:5]]
