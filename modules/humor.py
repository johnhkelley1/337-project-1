import settings

def get(year):
    joke_freq = {}
    for tweet in settings.data15:
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
