import random


SUITS = ["♠", "♥", "♦", "♣"]

RANKS = [
    "2", "3", "4", "5", "6", "7",
    "8", "9", "10", "J", "Q", "K", "A"
]


class Deck:

    def __init__(self):

        self.cards = []

        self.create()

        self.shuffle()

    def create(self):

        self.cards = []

        for suit in SUITS:

            for rank in RANKS:

                self.cards.append(
                    (rank, suit)
                )

    def shuffle(self):

        random.shuffle(self.cards)

    def deal_card(self):

        if len(self.cards) > 0:

            return self.cards.pop()

        return None

    def cards_left(self):

        return len(self.cards)


def create_deck():

    deck = Deck()

    return deck


def deal_player_cards(deck):

    return [
        deck.deal_card(),
        deck.deal_card()
    ]


def deal_flop(deck):

    return [
        deck.deal_card(),
        deck.deal_card(),
        deck.deal_card()
    ]


def deal_turn(deck):

    return deck.deal_card()


def deal_river(deck):

    return deck.deal_card()


def card_to_string(card):

    return f"{card[0]}{card[1]}"


def hand_to_string(cards):

    text = ""

    for card in cards:

        text += card_to_string(card)

        text += " "

    return text