import nltk
from nltk.tokenize.treebank import TreebankWordTokenizer

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

	stopwords = ['october','november','december','january','in','golden','globe','award','the','a','with']

	bigrams = nltk.bigrams(words)

	names = []

	for bigram in bigrams:
		if(bigram[0][0].isupper() and bigram[1][0].isupper() and bigram[0].lower() not in stopwords and bigram[1].lower() not in stopwords):
			names.append(bigram[0]+" "+bigram[1])
	return names

