import json

def init():
	global data15
	with open('gg2015.json') as data:
		data15 = json.load(data)

	# global synonyms = {
	# 	"motion picture": [
	# 		"film",
	# 		"movie"
	# 	],
	# 	"screenplay": [
	# 		"screenwriter",
	# 		"script",
	# 		"writer"
	# 	],
	# 	"series": [
	# 		"show"
	# 	],
	# 	"television": [
	# 		"tv"
	# 	],
	# 	"feature film": [
	# 		"movie",
	# 		"picture"
	# 	],
	# }