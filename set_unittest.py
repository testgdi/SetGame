import unittest
from SetCard import SetCard, SetDeck

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

    def test_showing_cards(self):
        """
        check that for a new deck, after dealing 1 card, showing has 1
        """
        self.d.deal_card()
        self.assertEqual( len( self.d.decklist), 80)

if __name__ == '__main__':
    unittest.main()
