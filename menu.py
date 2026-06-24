import pygame

class Menu:

    def __init__(self):

        self.start_button = pygame.Rect(
            550,
            500,
            300,
            100
        )

        self.help_button = pygame.Rect(
            550,
            620,
            300,
            80
        )

    def draw(self, screen, font):

        screen.fill((255,255,255))

        title = font.render(
            "TEXAS HOLD'EM",
            True,
            (0,0,0)
        )

        screen.blit(title, (420,150))

        pygame.draw.rect(
            screen,
            (0,180,0),
            self.start_button
        )

        pygame.draw.rect(
            screen,
            (0,0,180),
            self.help_button
        )

        screen.blit(
            font.render(
                "START",
                True,
                (255,255,255)
            ),
            (630,530)
        )

        screen.blit(
            font.render(
                "HELP",
                True,
                (255,255,255)
            ),
            (640,640)
        )