import requests
from bs4 import BeautifulSoup
import json

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

def getMovies():
	movies = []
	for j in range(4,5):
		for i in range(10):
			pg = i+1
			r = requests.get('https://api.themoviedb.org/3/discover/movie?primary_release_year=201'+str(j)+'&page='+str(pg)+'&sort_by=popularity.desc&api_key=4b65903b45a0d07cdf20f2317f081e1e')
			n_movies = json.loads(r.text)
			for movie in n_movies['results']:
				movies.append(movie['title'])
	print movies
	f = open('movies2.py','w')
	f.write(str(movies)) 
	f.close()

getMovies()
