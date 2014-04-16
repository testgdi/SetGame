import random

class SetCard:
    """a Set Game Card has 4 properties"""
    def __init__(self, number, fill, shape, color):
        self.number = number
        self.fill = fill
        self.shape = shape
        self.color = color

    def str(self):
        return ",".join([str( self.number),str( self.fill),\
                         str( self.shape), str(  self.color)])

class SetDeck:
    """ a deck of Set Game cards, all 81 of them
        stored in the property self.decklist
        some member functions to deal a card (pop)
        and shuffle the deck"""
        
    def __init__(self):
        self.decklist = []
        for n in range(1,4):
            for f in ["clear", "hashed", "solid"]:
                for s in ["oval","bean", "diamond"]:
                    for c in ["red", "grean", "blue"]:
                        self.decklist.append( SetCard(n,f, s, c))

    def printme(self):
        for c in self.decklist:
            print c.str()


    def pop(self):
        if len(self.decklist) >0:
            c = self.decklist[0]
            self.decklist = self.decklist[1:]
            return c
        else:
            return None

    def shuffle(self):
        random.shuffle(self.decklist)
        
def attrSet(c1,c2,c3, attr):
    """check if attr for 3 cards c1,c2,c3 are all different or all same
        return true or false"""
    # check n,f,s,c
    allsame = ( getattr(c1,attr) == getattr(c2,attr)) and \
              ( getattr(c2,attr) == getattr(c3,attr))
    
    alldiff = ( getattr(c1,attr) != getattr(c2,attr)) and \
              ( getattr(c2,attr) != getattr(c3,attr)) and \
              ( getattr(c3,attr) != getattr(c1,attr))

    return allsame or alldiff

def isSet(c1,c2,c3):
    """check all 4 attributes for 3 cards
        return true or false"""
    
    return attrSet(c1,c2,c3,"number") and \
           attrSet(c1,c2,c3,"shape") and \
           attrSet(c1,c2,c3,"fill") and \
           attrSet(c1,c2,c3,"color")
           
              

class SetGame:
    """ to play a game use this class and its functions
        there is a deck, you can deal out the 1st 12 cards
        these are the initial showing cards.
        Find all possible sets in the showing cards.

        a SetGame has a deck, and showing cards
        """
    
    def __init__(self):
        self.deck = SetDeck()

    def initial_12(self):
        self.showing = []
        for i in range(12):
            self.showing.append( self.deck.pop())


    def showingHaveSet(self):
        """ in a showing cards, check all choices of 3
            return the list of sets (may be more than one"""
        sets=[]
        for i in range(len(self.showing)-2):
            for j in range(i+1,len(self.showing)-1):
                for k in range(j+1, len( self.showing)):
                    c1,c2,c3 = self.showing[i],self.showing[j],self.showing[k]
                    if isSet(c1,c2,c3):
                        sets.append( (c1,c2,c3))
        return sets

if __name__ == "__main__":
    # shuffle the deck, deal out 12 showing, find the sets if any
    # in the 12 showing
    # print them out

    g = SetGame()
    g.deck.shuffle()
    g.initial_12()
    s = g.showingHaveSet()
    for x in s:
        print x[0].str(), x[1].str(), x[2].str()


    # calculate 1000 games, how are many without set in initial 12

    count = 0
    for i in range(1000):
        g = SetGame()
        g.deck.shuffle()
        g.initial_12()
        s = g.showingHaveSet()
        if len(s) == 0:
            count += 1
    print count
        
