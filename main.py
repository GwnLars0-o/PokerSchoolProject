import pygame

from screens.menu import Menu
from screens.help import HelpScreen
from screens.rules import RulesScreen
from screens.manual import ManualScreen
from screens.game import Game
from screens.gameover import GameOverScreen

pygame.init()

WIDTH = 1400
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Texas Hold'em")

font = pygame.font.SysFont(None, 45)

clock = pygame.time.Clock()

# schermen
menu = Menu()
help_screen = HelpScreen()
rules_screen = RulesScreen()
manual_screen = ManualScreen()
game = Game()
gameover_screen = GameOverScreen()

# mogelijke states
state = "menu"

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            # MENU
            if state == "menu":

                if menu.start_button.collidepoint(pos):

                    game.reset_game()

                    state = "game"

                elif menu.help_button.collidepoint(pos):

                    state = "help"

            # HELP
            elif state == "help":

                if help_screen.back_button.collidepoint(pos):

                    state = "menu"

                elif help_screen.handleiding_button.collidepoint(pos):

                    state = "manual"

                elif help_screen.rules_button.collidepoint(pos):

                    state = "rules"

            # HANDLEIDING
            elif state == "manual":

                if manual_screen.back_button.collidepoint(pos):

                    state = "help"

            # WINCONDITIES
            elif state == "rules":

                if rules_screen.back_button.collidepoint(pos):

                    state = "help"

            # SPEL
            elif state == "game":

                game.handle_click(pos)

                if game.game_over:

                    state = "gameover"

            # GAME OVER / WIN
            elif state == "gameover":

                if gameover_screen.button_clicked(pos):

                    state = "menu"

    # tekenen van het juiste scherm

    if state == "menu":

        menu.draw(screen, font)

    elif state == "help":

        help_screen.draw(screen, font)

    elif state == "manual":

        manual_screen.draw(screen, font)

    elif state == "rules":

        rules_screen.draw(screen, font)

    elif state == "game":

        game.draw(screen, font)

    elif state == "gameover":

        if game.player_won:

            screen.fill((0, 60, 0))

            big_font = pygame.font.SysFont(None, 120)

            text = big_font.render(
                "YOU WIN",
                True,
                (0, 255, 0)
            )

            screen.blit(text, (470, 250))

            pygame.draw.rect(
                screen,
                (200, 200, 200),
                gameover_screen.back_button
            )

            screen.blit(
                font.render(
                    "TERUG NAAR MENU",
                    True,
                    (0, 0, 0)
                ),
                (575, 525)
            )

        else:

            gameover_screen.draw(screen, font)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()