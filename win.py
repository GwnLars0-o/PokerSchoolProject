import pygame


class WinScreen:

    def __init__(self):

        self.back_button = pygame.Rect(
            550,
            500,
            300,
            80
        )

    def draw(self, screen, font):

        screen.fill((0, 60, 0))

        title_font = pygame.font.SysFont(
            None,
            120
        )

        win_text = title_font.render(
            "YOU WIN",
            True,
            (0, 255, 0)
        )

        screen.blit(
            win_text,
            (430, 250)
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