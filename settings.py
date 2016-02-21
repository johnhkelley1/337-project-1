import json

def init():
	global data15
	global awards
	global synonyms
	global award_stopwords
	with open('gg2015.json') as data:
		data15 = json.load(data)

	awards = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
	award_stopwords = ['in','a','the','-','or','for']

	synonyms = {
		"motion picture": [
			"film",
			"movie"
		],
		"screenplay": [
			"screenwriter",
			"script",
			"writer"
		],
		"series": [
			"show"
		],
		"television": [
			"tv"
		],
		"feature film": [
			"movie",
			"picture"
		],
	}