import requests
from bs4 import BeautifulSoup
import settings
import nltk
from nltk.tokenize import *
import awards
from collections import defaultdict
#import award_name_from_text
import util
import settings



# def award_name_from_text(text):
# 	words = word_tokenize(text)
# 	for i,val in enumerate(words):
# 		if val != 'Best':
# 			continue
# 			if i>=(len(words) - 2):
#    	break
#   	if words[i+1].istitle() == False:
#    	continue
#    award = val
#    i+=1
#      firsthyph = True
#      while words[i].istitle() or (words[i] == "-" and firsthyph == True):
#      	if words[i] == "-":
#      		firsthyph = False
#      		award = award+" "+words[i]
#        i+=1
#        if (i)>=(len(words) - 1):
#        	break
#         if len(word_tokenize(award)) > 3:
#         	return award
#         return 0
#  return 0

def award_name_from_text(text):
    words = word_tokenize(text)
    for i,val in enumerate(words):
        if val != 'Best':
            continue
        if i>=(len(words) - 2):
            break
        if words[i+1].istitle() == False:
            continue
        award = val
        i+=1
        firsthyph = True
        while words[i].istitle() or (words[i] == "-" and firsthyph == True):
            if words[i] == "-":
                firsthyph = False
            award = award+" "+words[i]
            i+=1
            if (i)>=(len(words) - 1):
                break
        if len(word_tokenize(award)) > 3:
            return award
        return 0
    return 0

def name_from_text(text):
    words = word_tokenize(text)
    name = ''
    for i,val in enumerate(words):

        if words[i].istitle() == True and (i + 1) < len(words):
        	while words[i].istitle():
        		name = name + " " + words[i]
        		i+=1
        		if (i) >= (len(words) - 1):
        			break
        	if len(word_tokenize(name)) >=1:
        		return name
        	return 0

        return 0

def get(year):
	#tweetsToLookAt = []
	#potentialPresenters = []
	#potentialAwardsArea = []
	tknzr = TweetTokenizer()
	#s1 = tknzr.tokenize(tweet)
	#tweetsToLookAt.append(tweet)
	awards = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 
	'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 
	'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 
	'best performance by an actor in a supporting role in a motion picture', 
	'best director - motion picture', 'best screenplay - motion picture', 
	'best original score - motion picture', 'best original song - motion picture', 
	'best television series - drama', 'best performance by an actress in a television series - drama', 
	'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 
	'best performance by an actress in a television series - comedy or musical', 
	'best performance by an actor in a television series - comedy or musical', 
	'best mini-series or motion picture made for television', 
	'best performance by an actress in a mini-series or motion picture made for television', 
	'best performance by an actor in a mini-series or motion picture made for television', 
	'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 
	'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
	award_stopwords = ['in','a','the','-','or','for']
	award_words = ['Best', 'best', 'Motion', 'motion', 'Picture', 'picture', 'Drama', 'drama', 'Performance', 'performance', 'Actress', 'actress', 'Actor', 'actor','Comedy', 'comedy', 'Musical', 'musical', 'Animated', 'animated', 'Feature', 'feature', 'Film', 'film', 'Foreign', 'foreign', 'Language', 'language', 'Supporting', 'supporting', 'Role', 'role', 'Director', 'director', 'Screenplay', 'screenplay', 'Original', 'orginal', 'Score', 'score', 'Song', 'song', 'Television', 'television', 'Series', 'series', 'Mini-series',  'mini-series', 'mini', 'Mini']
 

	dylan_awards = []
	dylan_awards2= []
	dylan_names = []
	presenters_awards = defaultdict(list)

	#need list of names of people.
	#list of names of awards 

	if year == '2015':
		data = settings.data15
	else:
		data = settings.data13

	for tweet in data:
		if 'will be presented by' in tweet['text']:
			#AWARD / PERSON
			
			str0 = tweet['text']
			awardPerson = str0.split('will be presented by')
			if len(awardPerson) == 2:
				award = awardPerson[0]
				person = awardPerson1[1]
				dylan_awards.append(award_name_from_text(award))
				presenter = name_from_text(person)
				dylan_names.append(presenter)

				s1Award = tknzr.tokenize(award)
				if len(set(award_words).intersection(set(s1Award))) >= 2:
					worWards = set(award_words).intersection(set(s1Award))
					#dylan_awards2.append(set(award_words).intersection(set(s1Award)))
					maxScore = 0
					chosenAward = '' 
					for award in awards:
						sampleStrings = tknzr.tokenize(award)
						score = len(set(sampleStrings).intersection(set(worWards)))
						if score > maxScore:
							maxScore = score
							chosenAward = award
					if not (chosenAward == ''):
						dylan_awards2.append(chosenAward)



		elif 'will be presenting' in tweet['text']:
			#PERSON / AWARD
			str1 = tweet['text']
			personAward = str.split('will be presenting')
			if len(personAward) == 2:
				person = personAward[0]
				award = personAward[1]
				dylan_awards.append(award_name_from_text(award))
				presenter = name_from_text(person)
				dylan_names.append(presenter)
				s1Award = tknzr.tokenize(award)
				if len(set(award_words).intersection(set(s1Award))) >= 2:
					worWards = set(award_words).intersection(set(s1Award))
					#dylan_awards2.append(set(award_words).intersection(set(s1Award)))
					maxScore = 0
					chosenAward = '' 
					for award in awards:
						sampleStrings = tknzr.tokenize(award)
						score = len(set(sampleStrings).intersection(set(worWards)))
						if score > maxScore:
							maxScore = score
							chosenAward = award
					if not (chosenAward == ''):
						dylan_awards2.append(chosenAward)

		elif 'presented by' in tweet['text']:
			#AWARD / PERSON
			str2 = tweet['text']
			awardPerson1 = str2.split('presented by')
			if len(awardPerson1) == 2:
				award = awardPerson1[0]
				person = awardPerson1[1]
				dylan_awards.append(award_name_from_text(award))
				presenter = name_from_text(person)
				dylan_names.append(presenter)
				s1Award = tknzr.tokenize(award)
				if len(set(award_words).intersection(set(s1Award))) >= 2:
					worWards = set(award_words).intersection(set(s1Award))
					#dylan_awards2.append(set(award_words).intersection(set(s1Award)))
					maxScore = 0
					chosenAward = '' 
					for award in awards:
						sampleStrings = tknzr.tokenize(award)
						score = len(set(sampleStrings).intersection(set(worWards)))
						if score > maxScore:
							maxScore = score
							chosenAward = award
					if not (chosenAward == ''):
						dylan_awards2.append(chosenAward)
				
		elif 'is presenting' in tweet['text']:
			#PERSON / AWARD
			str3 = tweet['text']
			personAward1 = str3.split('is presenting')
			if len(personAward1) == 2:
				person = personAward1[0]
				award = personAward1[1]
				dylan_awards.append(award_name_from_text(award))
				presenter = name_from_text(person)
				dylan_names.append(presenter)
				s1Award = tknzr.tokenize(award)
				if len(set(award_words).intersection(set(s1Award))) >= 2:
					worWards = set(award_words).intersection(set(s1Award))
					#dylan_awards2.append(set(award_words).intersection(set(s1Award)))
					maxScore = 0
					chosenAward = '' 
					for award in awards:
						sampleStrings = tknzr.tokenize(award)
						score = len(set(sampleStrings).intersection(set(worWards)))
						if score > maxScore:
							maxScore = score
							chosenAward = award
					if not (chosenAward == ''):
						dylan_awards2.append(chosenAward)
		
		elif 'presents' in tweet['text']:
			#PERSON / AWARD	
			str4 = tweet['text']
			personAward2 = str4.split('presents')
			if len(personAward2) == 2:
				person = personAward2[0]
				award = personAward2[1]
				dylan_awards.append(award_name_from_text(award))
				presenter = name_from_text(person)
				dylan_names.append(presenter)
				s1Award = tknzr.tokenize(award)
				if len(set(award_words).intersection(set(s1Award))) >= 2:
					worWards = set(award_words).intersection(set(s1Award))
					#dylan_awards2.append(set(award_words).intersection(set(s1Award)))
					maxScore = 0
					chosenAward = '' 
					for award in awards:
						sampleStrings = tknzr.tokenize(award)
						score = len(set(sampleStrings).intersection(set(worWards)))
						if score > maxScore:
							maxScore = score
							chosenAward = award
					if not (chosenAward == ''):
						dylan_awards2.append(chosenAward)

		
		elif 'presented' in tweet['text']:
			#PERSON / AWARD	
			
			str5 = tweet['text']
			personAward3 = str5.split('presented')
			if len(personAward3) == 2:
				person = personAward3[0]
				award = personAward3[1]
				dylan_awards.append(award_name_from_text(award))
				presenter = name_from_text(person)
				dylan_names.append(presenter)
				s1Award = tknzr.tokenize(award)
				if len(set(award_words).intersection(set(s1Award))) >= 2:
					worWards = set(award_words).intersection(set(s1Award))
					#dylan_awards2.append(set(award_words).intersection(set(s1Award)))
					maxScore = 0
					chosenAward = '' 
					for award in awards:
						sampleStrings = tknzr.tokenize(award)
						score = len(set(sampleStrings).intersection(set(worWards)))
						if score > maxScore:
							maxScore = score
							chosenAward = award
					if not (chosenAward == ''):
						dylan_awards2.append(chosenAward)

	empty_list = []
	for index, name in enumerate(dylan_names):
		if (not(name == 0) and not(dylan_awards[index] == 0)):
			tempAward = dylan_awards[index]
			empty_list.append([tempAward, name])








	final_awards = set(dylan_awards2)
	dylan_awards_final = [e for e in dylan_awards if e != 0 ]			
	dylan_awwards_final_reduce = set(dylan_awards_final)
	# set of one selection of awards
	#print dylan_awwards_final_reduce
	#print "\n"
	#print dylan_awards2
	#print "\n"
	# set of other selection of awards
	#print final_awards
	#print "\n"
	#print presenters_awards
	#print dylan_names
	#print len(dylan_names)
	#print "\n"
	#print "======================================================"
	#print "======================================================"
	#print "\n"
	#print dylan_awards
	
	#print "======================================================"
	#print "======================================================"
	print "======================================================"
	print "======================================================"
	print empty_list
	awards2 = {}
	for item in empty_list:
		awards2[item[0]] = item[1]

	return awards2





