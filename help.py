import pygame


class HelpScreen:

    def __init__(self):

        self.back_button = pygame.Rect(
            20,20,150,60
        )

        self.handleiding_button = pygame.Rect(
            450,250,500,100
        )

        self.rules_button = pygame.Rect(
            450,450,500,100
        )

    def draw(self, screen, font):

        screen.fill((255,255,255))

        title_font = pygame.font.SysFont(
            None,
            90
        )

        title = title_font.render(
            "HELP",
            True,
            (0,0,0)
        )

        screen.blit(title,(560,80))

        pygame.draw.rect(
            screen,
            (0,150,255),
            self.handleiding_button
        )

        pygame.draw.rect(
            screen,
            (0,180,0),
            self.rules_button
        )

        pygame.draw.rect(
            screen,
            (200,0,0),
            self.back_button
        )

        screen.blit(
            font.render(
                "HANDLEIDING",
                True,
                (255,255,255)
            ),
            (580,285)
        )

        screen.blit(
            font.render(
                "WINCONDITIES",
                True,
                (255,255,255)
            ),
            (570,485)
        )

        screen.blit(
            font.render(
                "BACK",
                True,
                (255,255,255)
            ),
            (55,35)
        )