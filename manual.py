import pygame


class ManualScreen:

    def __init__(self):

        self.back_button = pygame.Rect(
            20,20,150,60
        )

    def draw(self,screen,font):

        screen.fill((255,255,255))

        title_font = pygame.font.SysFont(
            None,
            70
        )

        title = title_font.render(
            "HANDLEIDING",
            True,
            (0,0,0)
        )

        screen.blit(title,(470,50))

        regels = [

            "Je begint met 3 bots en 1000 euro.",

            "Iedere speler krijgt 2 kaarten.",

            "Small Blind = 5",

            "Big Blind = 10",

            "CALL = meegaan met de inzet.",

            "RAISE = inzet verhogen.",

            "FOLD = kaarten opgeven.",

            "Bij fold kan je de ronde niet meer winnen.",

            "Het spel eindigt wanneer jij of alle bots",
            "geen geld meer hebben."

        ]

        y = 180

        for regel in regels:

            tekst = font.render(
                regel,
                True,
                (0,0,0)
            )

            screen.blit(
                tekst,
                (120,y)
            )

            y += 55

        pygame.draw.rect(
            screen,
            (200,0,0),
            self.back_button
        )

        screen.blit(
            font.render(
                "BACK",
                True,
                (255,255,255)
            ),
            (55,35)
        )