"""BlackJack game"""
import random    #TODO: Remove the star


class Card(object):

    card_values = {
        'QS': 10, '9S': 9, 'KS': 10, 'AS': (11, 1), '7S': 7, '2S': 2, '6S': 6, '10S': 10, 'JS': 10, '4S': 4, '8S': 8, '3S': 3, '5S': 5,
        'QC': 10, '9C': 9, 'KC': 10, 'AC': (11, 1), '7C': 7, '2C': 2, '6C': 6, '10C': 10, 'JC': 10, '4C': 4, '8C': 8, '3C': 3, '5C': 5,
        'QH': 10, '9H': 9, 'KH': 10, 'AH': (11, 1), '7H': 7, '2H': 2, '6H': 6, '10H': 10, 'JH': 10, '4H': 4, '8H': 8, '3H': 3, '5H': 5,
        'QD': 10, '9D': 9, 'KD': 10, 'AD': (11, 1), '7D': 7, '2D': 2, '6D': 6, '10D': 10, 'JD': 10, '4D': 4, '8D': 8, '3D': 3, '5D': 5
        }

    def __init__(self, name):
        suit, rank = name[0], name[1]    #  9S
        self.suit = suit
        self.rank = rank
        self.name = name

        self.value = Card.card_values[name]

    def __str__(self):
        return "The cards is the {} of {}.".format(self.value, self.name)

    def __repr__(self):
        return "{1} worth {0}".format(self.value, self.name)

    def __add__(self, other_card):
        return self.value + other_card.value

    def __radd__(self, total):
        return self.value + total


class Deck(object):

    def __init__(self, quantity=52, decks=1):

        # ranks = list(range(1, 11)) + list('JQKA')
        # suits = ('C', 'S', 'H', 'D')
        # cards = [Card(name=s+r) for s in suits for r in ranks]
        cards = [Card(name) for name in Card.card_values] * decks
        #import pdb; pdb.set_trace()
        self.cards = cards
        #Card(range(number))

    def __str__(self):
        return "This deck has {0} cards.".format(len(self.cards))

    def __repr__(self):
        return "{0}cards".format(len(self.cards))

    def shuffle(self):
        old_hole = list(self.cards.copy())
        hole_cards = list()

        while len(old_hole) > 0:
            # hole = random.choice(cards)
            import pdb; pdb.set_trace()
            choice = random.randint(0, (len(old_hole)))
            card = old_hole.pop(choice)
            hole_cards.append(card)

        self.cards = hole_cards
        return self

    def cut(self):
        a , b = hole_cards[:26], hole_cards[26:]
        cut_cards = b + a
        return self

    def draw_top(self):
        card = self.cards.pop(0)
        return card


class Player(object):

    def __init__(self, name, hand, dealer=False):
        self.name = name
        self.hand = hand
        self.dealer = dealer


class Deal(object):

    def __init__(self, game, players, deck):
        self.game = game
        self.players = players

    def deal(self, rounds=2, game='black_jack'):
        for _ in range(rounds):
            for player in self.players:
                card = deck.draw_top()
                player.hand.add_card(card)



        # if number of players > 4 two decks?
        # clean_cards = deck.shuffle().cut()
        #cut()
        # players = dict()
        # player = list()
        # dictionary of Player:cards
        # #player = list()
        # if game == black_jack:
        #     for player in num_players:
        #         player.append(clean_cards.pop(0))
            #cut_cards.pop(0)


class Hand(object):

    def __init__(self, cards=None):
        if cards is None:
            self.cards = list()
        else:
            self.cards = cards

    def __str__(self):
        print("Each player has {} cards in their hand".format(cards_per))

    def score(self):
        pass

    def add_card(self, card):
        self.cards.append(card)
        return self


##############################3
#
# def black_jack(num_players):
#     Deck.shuffle().cut().deal()
#
#     print(player)
#
# black_jack(3)


def deal_round(deck, player, dealer):
    pass




def sit():
    """
    Runs the table.
    """

    print("Welcome  > ")

    deck = Deck()
    deck.shuffle()
    deck.cut()

    print("dealing...")
    time.sleep(2)

    phand = Hand()
    player = Player(name='jason', hand=phand)

    dhand = Hand()
    dealer = Player(name='kieran', hand=dhand)

    deal = Deal(deck=deck)
    deal.deal()

sit()
