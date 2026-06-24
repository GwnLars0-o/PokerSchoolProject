import pygame


class SoundManager:

    def __init__(self):

        pygame.mixer.init()

        self.enabled = True

        self.click = None
        self.win = None
        self.lose = None
        self.deal = None

        self.load_sounds()

    def load_sounds(self):

        try:
            self.click = pygame.mixer.Sound(
                "assets/click.wav"
            )
        except:
            pass

        try:
            self.win = pygame.mixer.Sound(
                "assets/win.wav"
            )
        except:
            pass

        try:
            self.lose = pygame.mixer.Sound(
                "assets/lose.wav"
            )
        except:
            pass

        try:
            self.deal = pygame.mixer.Sound(
                "assets/deal.wav"
            )
        except:
            pass

    def play_click(self):

        if self.click:
            self.click.play()

    def play_win(self):

        if self.win:
            self.win.play()

    def play_lose(self):

        if self.lose:
            self.lose.play()

    def play_deal(self):

        if self.deal:
            self.deal.play()

    def toggle(self):

        self.enabled = not self.enabled

        if self.enabled:
            pygame.mixer.unpause()
        else:
            pygame.mixer.pause()