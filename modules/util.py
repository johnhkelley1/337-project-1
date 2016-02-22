import nltk
from nltk.tokenize.treebank import TreebankWordTokenizer
import movie_data

def year2num(year):
	num = int(year) - 1943
	return num

def year2suf(year):
	num = year2num(year)
	dig = num % 10
	num = str(num)
	if dig == 1:
		return num+"st"
	elif dig == 2:
		return num+"nd"
	elif dig == 3:
		return num+"rd"
	return num+"th"

def names_from_text(text):
	word_tokenize = nltk.tokenize.TreebankWordTokenizer().tokenize
	words = word_tokenize(text)

	stopwords = ['if','october','november','december','january','in','golden','globe','globes','goldenglobes','goldenglobe','award','the','a','with','tv','red','carpet','hilton','best','series','actor','actress','motion','motion','picture']

	words = [w for w in words if w not in stopwords]


	bigrams = nltk.bigrams(words)

	names = []

	for bigram in bigrams:
		if(bigram[0][0].isupper() and bigram[1][0].isupper() and bigram[0].lower() not in stopwords and bigram[1].lower() not in stopwords):
			names.append(bigram[0]+" "+bigram[1])
	return names

def get_human_names(text):
	names = names_from_text(text)
	names = [name.title() for name in names]
	act_names = []
	for name in names:
		if name in movie_data.actors:
			act_names.append(name)
	return act_names


