import requests
from bs4 import BeautifulSoup

def getActors():
	r = requests.get('http://www.imdb.com/list/ls058011111/')
	soup = BeautifulSoup(r.text, 'html.parser')
	actors = []
	for a in soup.find_all('div', { "class" : "info" }):
		#if a.parent.parent.has_attr('info'):
		soup2 = BeautifulSoup(a.text, 'html.parser')

		name = a.find('a').text

		actors.append(name)

	for i in range(9):
		r = requests.get('http://www.imdb.com/list/ls058011111/?start='+str(i+1)+'01')
		soup = BeautifulSoup(r.text, 'html.parser')
		for a in soup.find_all('div', { "class" : "info" }):
		#if a.parent.parent.has_attr('info'):
			soup2 = BeautifulSoup(a.text, 'html.parser')

			name = a.find('a').text

			actors.append(name)

	print actors

getActors()
