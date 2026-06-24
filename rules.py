import pygame


class RulesScreen:

    def __init__(self):

        self.back_button = pygame.Rect(
            20,20,150,60
        )

    def draw(self,screen,font):

        screen.fill((255,255,255))

        title_font = pygame.font.SysFont(
            None,
            80
        )

        screen.blit(
            title_font.render(
                "WINCONDITIES",
                True,
                (0,0,0)
            ),
            (430,40)
        )

        handen = [

            "1 Pair        ♥A ♠A",

            "2 Two Pair    ♥A ♠A ♦5 ♣5",

            "3 Three of a Kind    ♥A ♠A ♦A",

            "4 Straight    5 6 7 8 9",

            "5 Flush       ♥2 ♥5 ♥7 ♥J ♥K",

            "6 Full House  A A A 5 5",

            "7 Four of a Kind  A A A A",

            "8 Straight Flush ♥5 ♥6 ♥7 ♥8 ♥9",

            "9 Royal Flush ♥10 ♥J ♥Q ♥K ♥A"

        ]

        y = 140

        for hand in handen:

            txt = font.render(
                hand,
                True,
                (0,0,0)
            )

            screen.blit(
                txt,
                (120,y)
            )

            y += 60

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