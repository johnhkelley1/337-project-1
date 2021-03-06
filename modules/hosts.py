from modules import util
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize.treebank import TreebankWordTokenizer
import util
import settings
import sys

def get(year):
	num = util.year2suf(year)
	r = requests.get('https://en.wikipedia.org/wiki/'+num+'_Golden_Globe_Awards')
	soup = BeautifulSoup(r.text, 'html.parser')

	text = soup.text
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

	sentences = tokenizer.tokenize(text)

	host_sent = ""

	word_tokenize = nltk.tokenize.TreebankWordTokenizer().tokenize

	for sentence in sentences:
		ishost = False
		for word in word_tokenize(sentence):
			if 'host' in word:
				ishost = True
		if ishost:
			host_sent = sentence
			break

	return util.names_from_text(host_sent)

def getFromTweets(year):
	names = {}
	hosts = []
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
		if 'host' not in tweet['text']:
			continue
		tnames = util.names_from_text(tweet['text'])
		for tname in tnames:
			if tname in names:
				names[tname] += 1
			else:
				names[tname] = 1
	hosts = sorted(names, key=names.get, reverse=True)
	maxc = names[hosts[0]]
	for i,val in enumerate(hosts):
		if names[val] < .8*maxc:
			hosts = hosts[:i]
			break
	return hosts
