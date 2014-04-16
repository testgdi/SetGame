from SetCard import *
"""
Monte Carlo simulation of many games.
play the game until deck is used up and no
more sets are to be found in the showing cards.
Count the number of showing cards left over
"""

def leftOver():
    """
    returns the number of cards left over at the end of a game
    """
    
    # set up the game, shuffle, deal out 12 cards
    g = SetGame()
    g.deck.shuffle()
    g.initial_12()

    # list of cards not yet dealt in g.deck.decklist
    # list of cards face up on table in g.showing

    while len( g.deck.decklist) > 0:
        # check if the showing cards have a set
        # showingHaveSet returns list of all possible
        # sets in the showing cards
        # but a given card might belong to more than one of these.
        # if there is a set, take 1st group of 3 from list of possible
        # sets, remove those 3 cards from the showing cards
        # then deal out 3 more cards from the deck.
        # do this until the deck is empty
        s = g.showingHaveSet()
        while len( s) > 0 and len( g.showing) > 0:
            for c in s[0]:
                g.showing.remove( c)

            s = g.showingHaveSet()

        # add 3 cards to showing
        for i in range(3):
            g.showing.append( g.deck.pop())

    # deck is empty, now remove any remaining sets from g.showing
    s = g.showingHaveSet()
    while (len( s) > 0):
        # remove the set from the showing cards
        for c in s[0]:
            g.showing.remove( c)

        # check if there are any more sets in the remaining showing cards
        s = g.showingHaveSet()

    # can't remove any more sets from the showing, so return how many left
    return len( g.showing)

if __name__ == "__main__":
    nSim = 2000
    leftShowing = {} # dictionary to hold leftover:count pairs
    for i in range(nSim):
        # simulate complete game and return how many left over
        lo = leftOver() 
        if not leftShowing.has_key(lo):
            leftShowing[lo] = 0
        leftShowing[lo] += 1

    # to print in order, sort keys in dict
    lsk = leftShowing.keys()
    lsk.sort()
    for x in lsk:
        print x, leftShowing[x], float(leftShowing[x])/nSim
        
        
