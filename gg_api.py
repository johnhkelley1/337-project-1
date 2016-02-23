'''Version 0.2'''

from modules import awards
from modules import hosts
from modules import nominees
from modules import winners
from copy import deepcopy
import settings
import movie_data

settings.init()
movie_data.init()

OFFICIAL_AWARDS = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']

def get_hosts(year):
    '''Hosts is a list of one or more strings. Do NOT change the name
    of this function or what it returns.'''
    print 'hosts'
    # Your code here
    return hosts.getFromTweets(year)

def get_awards(year):
    '''Awards is a list of strings. Do NOT change the name
    of this function or what it returns.'''
    print 'awards'
    # Your code here
    #return awards.getFromTweets(year)
    return OFFICIAL_AWARDS

def get_nominees(year):
    '''Nominees is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change
    the name of this function or what it returns.'''
    print 'nominees'
    # Your code here
    winners = {}
    for award in OFFICIAL_AWARDS:
        winners[award] = ["Daniel Craig","Jack Black"]
    return nominees.get(year)
    #return winners

def get_winner(year):
    '''Winners is a dictionary with the hard coded award
    names as keys, and each entry containing a single string.
    Do NOT change the name of this function or what it returns.'''
    print 'winners'
    #Your code here
    winners = {}
    for award in OFFICIAL_AWARDS:
        winners[award] = "Daniel Craig"

    # return winners.get(year)
    return winners

def get_presenters(year):
    '''Presenters is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change the
    name of this function or what it returns.'''
    print 'presenters'
    # Your code here
    winners = {}
    for award in OFFICIAL_AWARDS:
        winners[award] = ["Daniel Craig","Jack Black"]
    return winners

def pre_ceremony():
    '''This function loads/fetches/processes any data your program
    will use, and stores that data in your DB or in a json, csv, or
    plain text file. It is the first thing the TA will run when grading.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    print "Pre-ceremony processing complete."
    return

def main():
    '''This function calls your program. Typing "python gg_api.py"
    will run this function. Or, in the interpreter, import gg_api
    and then run gg_api.main(). This is the second thing the TA will
    run when grading. Do NOT change the name of this function or
    what it returns.'''

    choices = [{
        'choice': 'View Winners',
        'function': 'get_winner'
    }, {
        'choice': 'View Nominees',
        'function': 'get_nominees'
    }, {
        'choice': 'View Awards',
        'function': 'get_awards'
    }, {
        'choice': 'View Presenters',
        'function': 'get_presenters'
    }, {
        'choice': 'View Hosts',
        'function': 'get_hosts'
    }]

    while True:
        for i, choice in enumerate(choices):
            print "(%s) %s" % (i, choice['choice'])
        print "(q) Quit"

        print "Select a choice:",

        choice = raw_input()
        if choice == 'q':
            break

        choice = int(choice)
        results = globals()[choices[choice]['function']](2015)
        for key, val in results.iteritems():
            print "=== %s ===" % key
            print val

    return

if __name__ == '__main__':
    main()
