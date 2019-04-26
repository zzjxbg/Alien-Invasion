import pygame
from pygame.sprite import Sprite


class Player(Sprite):

    def __init__(self, settings, screen):
        """ initialize player and set its position to the center """
        super(Player, self).__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/player.bmp')
        self.rect = self.image.get_rect()
        self.rec = screen.get_rect()

        self.rect.centerx = self.rec.centerx
        self.rect.bottom = self.rec.bottom

        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def set_center(self):
        self.center = self.rec.centerx

    def update(self):

        if self.moving_right and self.rect.right < self.rec.right:
            self.center += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.player_speed

        self.rect.centerx = self.center

    def current(self):
        self.screen.blit(self.image, self.rect)
