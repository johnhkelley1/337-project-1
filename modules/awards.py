import requests
from bs4 import BeautifulSoup
import settings
import nltk
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
