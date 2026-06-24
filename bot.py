import random

class Bot:

    def __init__(self, name):

        self.name = name

        self.money = 1000

        self.cards = []

        self.folded = False

        self.current_bet = 0

    def reset_round(self):

        self.cards = []

        self.folded = False

        self.current_bet = 0

    def receive_cards(self, card1, card2):

        self.cards = [card1, card2]

    def pay_blind(self, amount):

        if self.money >= amount:

            self.money -= amount

            self.current_bet += amount

            return amount

        paid = self.money

        self.money = 0

        self.current_bet += paid

        return paid

    def call(self, highest_bet):

        amount_needed = highest_bet - self.current_bet

        if amount_needed <= 0:
            return 0

        if self.money >= amount_needed:

            self.money -= amount_needed

            self.current_bet += amount_needed

            return amount_needed

        paid = self.money

        self.current_bet += paid

        self.money = 0

        return paid

    def raise_bet(self, highest_bet):

        raise_amount = random.choice(
            [10, 20, 30, 40]
        )

        total_needed = (
            highest_bet
            - self.current_bet
            + raise_amount
        )

        if self.money >= total_needed:

            self.money -= total_needed

            self.current_bet += total_needed

            return total_needed

        paid = self.money

        self.current_bet += paid

        self.money = 0

        return paid

    def fold(self):

        self.folded = True

    def make_decision(self, highest_bet):

        if self.folded:
            return ("fold", 0)

        decision = random.randint(1, 100)

        if decision <= 60:

            amount = self.call(highest_bet)

            return ("call", amount)

        elif decision <= 80:

            amount = self.raise_bet(highest_bet)

            return ("raise", amount)

        else:

            self.fold()

            return ("fold", 0)

    def is_bankrupt(self):

        return self.money <= 0