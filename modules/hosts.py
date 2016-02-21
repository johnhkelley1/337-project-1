from modules import util
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize.treebank import TreebankWordTokenizer

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