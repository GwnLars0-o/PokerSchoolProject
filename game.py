import pygame

from cards import (
    create_deck,
    deal_player_cards,
    deal_flop,
    deal_turn,
    deal_river,
    hand_to_string
)

from poker import determine_winner

from bot import Bot


class Game:

    def __init__(self):

        self.reset_game()

    def reset_game(self):

        self.player_money = 1000

        self.pot = 0

        self.current_bet = 10

        self.player_bet = 0

        self.player_folded = False

        self.game_over = False

        self.player_won = False

        self.deck = create_deck()

        self.bot1 = Bot("Bot 1")
        self.bot2 = Bot("Bot 2")
        self.bot3 = Bot("Bot 3")

        self.player_cards = deal_player_cards(
            self.deck
        )

        self.bot1.cards = deal_player_cards(
            self.deck
        )

        self.bot2.cards = deal_player_cards(
            self.deck
        )

        self.bot3.cards = deal_player_cards(
            self.deck
        )

        self.community_cards = []

        flop = deal_flop(self.deck)

        for card in flop:
            self.community_cards.append(card)

        self.community_cards.append(
            deal_turn(self.deck)
        )

        self.community_cards.append(
            deal_river(self.deck)
        )

        self.small_blind()

        self.big_blind()

        self.create_buttons()

    def create_buttons(self):

        self.call_button = pygame.Rect(
            400,
            720,
            150,
            50
        )

        self.raise_button = pygame.Rect(
            620,
            720,
            150,
            50
        )

        self.fold_button = pygame.Rect(
            840,
            720,
            150,
            50
        )

    def small_blind(self):

        blind = 5

        self.player_money -= blind

        self.player_bet += blind

        self.pot += blind

    def big_blind(self):

        blind = 10

        self.bot1.money -= blind

        self.bot1.current_bet += blind

        self.pot += blind

    def call(self):

        difference = (
            self.current_bet
            - self.player_bet
        )

        if difference <= 0:
            return

        if self.player_money >= difference:

            self.player_money -= difference

            self.player_bet += difference

            self.pot += difference

    def raise_bet(self):

        raise_amount = 20

        total = (
            self.current_bet
            - self.player_bet
            + raise_amount
        )

        if self.player_money >= total:

            self.player_money -= total

            self.player_bet += total

            self.current_bet += raise_amount

            self.pot += total

    def fold(self):

        self.player_folded = True

        self.game_over = True

    def bot_turns(self):

        for bot in [
            self.bot1,
            self.bot2,
            self.bot3
        ]:

            action, amount = bot.make_decision(
                self.current_bet
            )

            self.pot += amount

    def determine_result(self):

        if self.player_folded:

            self.game_over = True

            self.player_won = False

            return

        winner, scores = determine_winner(

            self.player_cards,

            self.bot1.cards,

            self.bot2.cards,

            self.bot3.cards

        )

        if winner == "player":

            self.player_money += self.pot

            self.player_won = True

        else:

            self.player_won = False

        self.game_over = True

    def handle_click(self, pos):

        if self.game_over:
            return

        if self.call_button.collidepoint(pos):

            self.call()

            self.bot_turns()

            self.determine_result()

        elif self.raise_button.collidepoint(pos):

            self.raise_bet()

            self.bot_turns()

            self.determine_result()

        elif self.fold_button.collidepoint(pos):

            self.fold()

    def draw_buttons(self, screen, font):

        pygame.draw.rect(
            screen,
            (0, 150, 255),
            self.call_button
        )

        pygame.draw.rect(
            screen,
            (255, 180, 0),
            self.raise_button
        )

        pygame.draw.rect(
            screen,
            (220, 0, 0),
            self.fold_button
        )

        screen.blit(
            font.render(
                "CALL",
                True,
                (255,255,255)
            ),
            (440,730)
        )

        screen.blit(
            font.render(
                "RAISE",
                True,
                (255,255,255)
            ),
            (645,730)
        )

        screen.blit(
            font.render(
                "FOLD",
                True,
                (255,255,255)
            ),
            (875,730)
        )

    def draw(self, screen, font):

        screen.fill((0,120,0))

        title = font.render(
            "TEXAS HOLD'EM",
            True,
            (255,255,255)
        )

        screen.blit(title,(520,20))

        pot_text = font.render(
            f"POT: €{self.pot}",
            True,
            (255,255,255)
        )

        screen.blit(
            pot_text,
            (600,120)
        )

        money_text = font.render(
            f"Jouw geld: €{self.player_money}",
            True,
            (255,255,255)
        )

        screen.blit(
            money_text,
            (500,650)
        )

        player_cards = font.render(
            hand_to_string(
                self.player_cards
            ),
            True,
            (255,255,255)
        )

        screen.blit(
            player_cards,
            (550,600)
        )

        community = font.render(
            hand_to_string(
                self.community_cards
            ),
            True,
            (255,255,255)
        )

        screen.blit(
            community,
            (350,300)
        )

        screen.blit(
            font.render(
                "BOT 1",
                True,
                (255,255,255)
            ),
            (150,120)
        )

        screen.blit(
            font.render(
                "BOT 2",
                True,
                (255,255,255)
            ),
            (620,120)
        )

        screen.blit(
            font.render(
                "BOT 3",
                True,
                (255,255,255)
            ),
            (1080,120)
        )

        self.draw_buttons(
            screen,
            font
        )

        if self.game_over:

            if self.player_won:

                result = font.render(
                    "YOU WIN",
                    True,
                    (0,255,0)
                )

            else:

                result = font.render(
                    "GAME OVER",
                    True,
                    (255,0,0)
                )

            screen.blit(
                result,
                (500,450)
            )