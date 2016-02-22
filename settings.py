import json

def init():
	global data15
	global data13
	global awards
	global synonyms
	global award_stopwords
	print "Loading 2015 tweets into memory..."
	with open('gg2015.json') as data:
		data15 = json.load(data)
	print "Loading 2013 tweets into memory..."
	with open('gg2013.json') as data:
		data13 = json.load(data)

	awards = [
    {
        'name': 'cecil b. demille award',
        'regexs': ['cecil b\. demille'],
        'regex2':['cecil b. demille award'],
        'type': 0
    }, {
        'name': 'best motion picture - drama',
        'regexs': ['best motion picture.+drama'],
        'regex2':['best*(!actor&!actress)drama'],
        'type': 0
    }, {
        'name': 'best performance by an actress in a motion picture - drama',
        'regexs': ['best performance.+actress.+motion picture.+drama'],
        'regex2':[],
        'type': 1
    }, {
        'name': 'best performance by an actor in a motion picture - drama',
        'regexs': ['best performance by an actor in a motion picture.+drama'],
        'regex2':[],
        'type': 1
    }, {
        'name': 'best motion picture - comedy or musical',
        'regexs': ['best motion picture+.comedy or musical'],
        'regex2':[],
        'type': 0
    }, {
        'name': 'best performance by an actress in a motion picture - comedy or musical',
        'regexs': ['best performance.+actress.+motion picture.+comedy or musical'],
        'regex2':[],
        'type': 1
    }, {
        'name': 'best performance by an actor in a motion picture - comedy or musical',
        'regexs': ['best performance.+actor.+motion picture.+comedy or musical'],
        'regex2':[],
        'type': 1
    }, {
        'name': 'best animated feature film',
        'regexs': ['best animated feature film'],
        'regex2':[],
        'type': 0
    }, {
        'name': 'best foreign language film',
        'regexs' : ['best foreign language film'],
        'regex2':[],
        'type': 0
    }, {
        'name': 'best performance by an actress in a supporting role in a motion picture',
        'regexs': ['best performance.+actress.+supporting role.+motion picture'],
        'regex2':[],
        'type': 1
    }, {
        'name': 'best performance by an actor in a supporting role in a motion picture',
        'regexs': ['best performance.+actor.+supporting role.+motion picture'],
        'regex2':[],
        'type': 1
    }, {
        'name': 'best director - motion picture',
        'regexs': ['best director.+motion picture'],
        'regex2':[],
        'type': 1
    }, {
        'name': 'best screenplay - motion picture',
        'regexs': ['best screenplay.+motion picture'],
        'regex2':[],
        'type': 0
    }, {
        'name': 'best original score - motion picture',
        'regexs': ['best original score.+motion picture'],
        'regex2':[],
        'type': 0
    }, {
        'name': 'best original song - motion picture',
        'regexs': ['best original song.+motion picture'],
        'regex2':[],
        'type': 0
    }, {
        'name': 'best television series - drama',
        'regexs': ['best television series.+drama', 'best tv series.+drama'],
        'regex2':[],
        'type': 0
    }, {
        'name': 'best performance by an actress in a television series - drama',
        'regexs': ['best performance.+actress.+television series.+drama'],
        'type': 1
    }, {
        'name': 'best performance by an actor in a television series - drama',
        'regexs': ['best performance by an actor in a television series.+drama', 'best performance by an actor in a tv series.+drama'],
        'regex2':[],
        'type': 1
    }, {
        'name': 'best television series - comedy or musical',
        'regexs': ['best television series.+comedy or musical', 'best tv series.+comedy or musical'],
        'regex2':[],
        'type': 0
    }, {
        'name': 'best performance by an actress in a television series - comedy or musical',
        'regexs': ['best performance by an actress in a television series.+comedy or musical', 'best performance by an actress in a tv series.+comedy or musical'],
        'regex2':[],
        'type': 1
    }, {
        'name': 'best performance by an actor in a television series - comedy or musical',
        'regexs': ['best performance by an actor in a television series.+comedy or musical', 'best performance by an actor in a tv series.+comedy or musical'],
        'regex2':[],
        'type': 1
    }, {
        'name': 'best mini-series or motion picture made for television',
        'regexs': ['best mini-series or motion picture made for television', 'best mini-series or motion picture made for tv'],
        'regex2':[],
        'type': 0
    }, {
        'name': 'best performance by an actress in a mini-series or motion picture made for television',
        'regexs': ['best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for tv'],
        'regex2':[],
        'type': 1
    }, {
        'name': 'best performance by an actor in a mini-series or motion picture made for television',
        'regexs': ['best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for tv'],
        'regex2':[],
        'type': 1
    }, {
        'name': 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television',
        'regexs': ['best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for tv'],
        'regex2':[],
        'type': 1
    }, {
        'name': 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television',
        'regexs': ['best performance by an actor in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for tv'],
        'regex2':[],
        'type': 1
    }]
	award_stopwords = ['in','a','the','-','or','for','by','and']

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
