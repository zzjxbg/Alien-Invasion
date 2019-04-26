import pygame
from pygame.sprite import Sprite

class bullet(Sprite):


    def __init__(self, settings, screen, player):
        """ initialize bullets """
        super(bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_element = settings.bullet_speed

    def update(self):
        # Move the bullet up the screen and update it.
        self.y -= self.speed_element
        self.rect.y = self.y

    def bullet(self):
        # Draw the bullet
        pygame.draw.rect(self.screen, self.color, self.rect)
