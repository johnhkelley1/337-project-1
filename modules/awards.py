import requests
from bs4 import BeautifulSoup
import settings
def get():
	r = requests.get('https://en.wikipedia.org/wiki/Golden_Globe_Award')
	soup = BeautifulSoup(r.text, 'html.parser')
	names = []
	for a in soup.findAll('a'):
		if a.parent.name == 'li' and a.parent.text == a.text:
			if a.text.partition(' ')[0] == 'Best' or a.text.partition(' ')[0] == 'Cecil':
				names.append(a.parent.text)
	return names