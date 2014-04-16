SetCard.py defines classes for a Card, Deck and Game along with some
utility functions such as one that returns whether 3 cards constitute
a set. It then exercises these classes by running a montecarlo
simulation to find the probability that the initial 12 cards have no
set.

use-deck.py is a montecarlo simulation to find the probability of
there being no cards left showing at the end of a game. So it
simulates dealing the initial 12, removing sets and replacing cards
from the deck as needed.