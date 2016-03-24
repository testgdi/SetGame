from SetCard import *
"""
Monte Carlo simulation of many games.
play the game until deck is used up
Keep track of the max number of cards that
were ever showing at one time, i.e. immediately after
the start 12 cards are showing.
"""

def maxShowing():
    """
    returns the max numer of cards showing
    """
    
    # set up the game, shuffle, deal out 12 cards
    g = SetGame()
    g.deck.shuffle()
    g.initial_12()

    s = g.showingHaveSet()
    maxshowing = len( g.showing)
    while len( g.deck.decklist) > 0:
        while len( s) > 0 and len( g.showing) > 0:
            for c in s[0]:
                g.showing.remove( c)

            s = g.showingHaveSet()


        # add 3 cards to showing
        for i in range(3):
            g.showing.append( g.deck.deal_card())

        # update maxshowing and again see if there are any sets showing
        maxshowing = max( maxshowing, len(g.showing))
        s = g.showingHaveSet()

    # deck is empty, max showing has been updated

    return maxshowing

if __name__ == "__main__":
    nSim = 2000
    maxShowingDict = {} # dictionary to hold leftover:count pairs
    for i in range(nSim):
        ms = maxShowing() 
        if not maxShowingDict.has_key(ms):
            maxShowingDict[ms] = 0
        maxShowingDict[ms] += 1

    # to print in order, sort keys in dict
    lsk = maxShowingDict.keys()
    lsk.sort()
    print "max ever showing before removing sets"
    for x in lsk:
        print x, maxShowingDict[x]
        
        
