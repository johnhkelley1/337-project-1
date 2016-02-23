import requests
from bs4 import BeautifulSoup
import settings
import nltk
import sys
from nltk.tokenize.treebank import TreebankWordTokenizer

word_tokenize = nltk.tokenize.TreebankWordTokenizer().tokenize

def get():
	r = requests.get('https://en.wikipedia.org/wiki/Golden_Globe_Award')
	soup = BeautifulSoup(r.text, 'html.parser')
	names = []
	for a in soup.findAll('a'):
		if a.parent.name == 'li' and a.parent.text == a.text:
			if a.text.partition(' ')[0] == 'Best' or a.text.partition(' ')[0] == 'Cecil':
				names.append(a.parent.text)
	return names

def awards_from_text(text):
	awards = []
	for key in settings.awards:
		words = word_tokenize(text)
		stripkey = word_tokenize(key)
		stripkey = [w for w in stripkey if w not in settings.award_stopwords]
		words = [w.lower() for w in words]
		matches = 0
		for w in stripkey:
			if(w in words):
				matches += 1
		if matches > 3:
			awards.append(key)
	return awards

def award_name_from_text(text):
	words = word_tokenize(text)
	for i,val in enumerate(words):
		if val != 'Best':
			continue
		if i>=(len(words) - 2):
			break
		if words[i+1].istitle() == False:
			continue
		award = val
		i+=1
		firsthyph = True
		while words[i].istitle() or (words[i] == "-" and firsthyph == True):
			if words[i] == "-":
				firsthyph = False
			award = award+" "+words[i]
			i+=1
			if (i)>=(len(words) - 1):
				break
		if len(word_tokenize(award)) > 3:
			return award
		return 0
	return 0


def getFromTweets(year):
	awards = {}
	award_names = []
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
		aname = award_name_from_text(tweet['text'])
		if(aname != 0):
			if aname in awards:
				awards[aname] += 1
			else:
				awards[aname] = 1
			award_names = sorted(awards, key=awards.get, reverse=True)
			award_names = award_names[:30]
	print award_names
	return award_names
