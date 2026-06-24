import pygame


class GameOverScreen:

    def __init__(self):

        self.back_button = pygame.Rect(
            550,
            500,
            300,
            80
        )

    def draw(self, screen, font):

        screen.fill((40, 0, 0))

        title_font = pygame.font.SysFont(
            None,
            120
        )

        game_over_text = title_font.render(
            "GAME OVER",
            True,
            (255, 0, 0)
        )

        screen.blit(
            game_over_text,
            (350, 250)
        )

        pygame.draw.rect(
            screen,
            (200, 200, 200),
            self.back_button
        )

        button_text = font.render(
            "TERUG NAAR MENU",
            True,
            (0, 0, 0)
        )

        screen.blit(
            button_text,
            (575, 525)
        )

    def button_clicked(self, pos):

        return self.back_button.collidepoint(
            pos
        )