import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    
    def __init__(self, settings, screen):
        """ initialize alien """
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def endRow(self):
        # return true if alien at the end of the row
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        # update alien's position
        self.x += (self.settings.alien_speed * self.settings.direction)
        self.rect.x = self.x

    def current_location(self):
        self.screen.blit(self.image, self.rect)
