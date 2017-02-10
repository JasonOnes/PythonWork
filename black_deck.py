"""BlackJack game"""
from random import *


class Card(object):
    cards =
    {'QS': 10, '9S': 9, 'KS': 10, 'AS': (11, 1), '7S': 7, '2S': 2, '6S': 6, '10S': 10, 'JS': 10, '4S': 4, '8S': 8, '3S': 3, '5S': 5}
    {'QC': 10, '9C': 9, 'KC': 10, 'AC': (11, 1), '7C': 7, '2C': 2, '6C': 6, '10C': 10, 'JC': 10, '4C': 4, '8C': 8, '3C': 3, '5C': 5}
    {'QH': 10, '9H': 9, 'KH': 10, 'AH': (11, 1), '7H': 7, '2H': 2, '6H': 6, '10H': 10, 'JH': 10, '4H': 4, '8H': 8, '3H': 3, '5H': 5}
    {'QD': 10, '9D': 9, 'KD': 10, 'AD': (11, 1), '7D': 7, '2D': 2, '6D': 6, '10D': 10, 'JD': 10, '4D': 4, '8D': 8, '3D': 3, '5D': 5}

    def __init__(self, rank, suit, value):
        self.suit = suit
        self.value = value
        self.rank = rank

    def __str__(self):
        print("The cards is the {} of {}.".format(value, suit))

    def __repr__(self):
        print("{}of{}".format(value, suit))

class Deck(object):

    def __init__(self, number=52):
        self.self = self
        self.number = number
        #Card(range(number))

    def __str__(self):
        print("This deck has {} cards.".format(number))

    def __repr__(self):
        print("{}cards".format(number))

    def shuffle(self):
        old_hole = len(Deck)
        hole_cards = list()
        while old_hole > 0:
            hole = randint(len(numbers))
            old_hole -= old_hole
            hole_cards.append(hole)
        yield hole

    def cut(self):
        a , b = hole_cards[:26], hole_cards[26:]
        cut_cards = b + a

class Player(object):

    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

class Deal(object):

    def __init__(self, game, num_players=2):
        self.self = self
        self.game = game
        self.players = players

    def deal(self, game=black_jack):
        # if number of players > 4 two decks?
        Deck.shuffle().cut()
        #cut()
        players = dict()
        player = list()
        # dictionary of Player:cards
        #player = list()
        if game == black_jack:
            for player in num_players:
                player.append(cut_cards.pop(0))
            #cut_cards.pop(0)

class Hand(object):

    def __init__(self, num_players=2, cards_per=2):
        self.self = self
        self.num_players = num_players
        self.cards_per = cards_per

    def __str__(self):
        print("Each player has {} cards in their hand".format(cards_per))

def black_jack(num_players):
    Deck.shuffle().cut().deal()

    print(player)

black_jack(3)
