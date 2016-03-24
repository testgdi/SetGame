import unittest
from SetCard import SetCard, SetDeck, SetGame

class TestCardMethods( unittest.TestCase):

    def setUp(self):
        self.c = SetCard(number=3, fill="solid", shape="bean", color="red")
        

    def test_number_of_properties(self):
        """
        check that the number of properties is 4
        """
        self.assertEqual( len(self.c.__dict__), 4)

    def test_shape_is_bean(self):
        """
        check that the shape is bean from setup
        """        
        self.assertEqual( self.c.shape, 'bean')


class TestDeckMethods( unittest.TestCase):

    def setUp(self):
        self.d = SetDeck()

    def test_81_cards(self):
        """
        check that new deck has 81 cards
        """
        self.assertEqual( len( self.d.decklist), 81)

    def test_80_cards(self):
        """
        check that for a new deck, after dealing 1 card, deck now has 80 cards
        """
        self.d.deal_card()
        self.assertEqual( len( self.d.decklist), 80)

class TestGameMethods( unittest.TestCase):

    def setUp(self):
        self.g = SetGame()

    def test_showing_after_dealing(self):
        """
        check that for a new game, after dealing initial showing, showing has 12
        """
        self.g.initial_12()
        self.assertEqual( len( self.g.showing), 12)

    def test_deck_after_dealing(self):
        """
        check that for a new game, after dealing initial 12, deck 81-12=69
        """
        self.g.initial_12()
        self.assertEqual( len( self.g.deck.decklist), 69)

if __name__ == '__main__':
    unittest.main(verbosity=2)
