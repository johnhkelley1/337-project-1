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

	stopwords = ['rt', 'if','october','november','december','january','in',
		'golden','globe','globes','goldenglobes','goldenglobe','award','the','a'
		,'an','with','tv','television','red','carpet','hilton','best','series',
		'actor','actress','motion','picture','winner','supporting','comedy','or'
		,'role','imdb','performance','by','film','movie','musical','feature',
		'winners','awards','made','for','thr','winnner','musical.','mini-series'
		,'drama','congrats','huffingtonpost','presents','congratulations','wins'
		,'goldenglobes.','picture-comedy','gets','abc']

	words = [w for w in words if w.lower() not in stopwords]

	names  = []
	phrase = ""
	for word in words:
		if word[0].isupper():
			if len(phrase) != 0:
				phrase += " "
			phrase += word
		else:
			if len(phrase) > 0:
				names.append(phrase.lower())
				phrase = ""

	return names

def get_human_names(text):
	word_tokenize = nltk.tokenize.TreebankWordTokenizer().tokenize
	names = names_from_text(text)
	names = [name.title() for name in names if len(word_tokenize(name)) > 1]
	# act_names = []
	# for name in names:
	# 	if name in movie_data.actors:
	# 		act_names.append(name)
	return names
