import pygame.font
from pygame.sprite import Group

from player import Player


class record():


    def __init__(self, settings, screen, states):
        """Initialize record."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.states = states

        # Font settings
        self.text_color = (20, 20, 20)
        self.font = pygame.font.SysFont(None, 52)

        self.update_record()
        self.record()
        self.level()
        self.left_player()

    def update_record(self):
        # update grade and turn it into a image
        rounded_grade = int(round(self.states.grade, -1))
        grade_str = "{:,}".format(rounded_grade)
        self.grade_image = self.font.render(grade_str, True, self.text_color, self.settings.background_color)

       
        self.grade_rect = self.grade_image.get_rect()
        self.grade_rect.right = self.screen_rect.right - 20
        self.grade_rect.top = 20

    def record(self):
        high_grade = int(round(self.states.high_grade, -1))
        high_grade_str = "{:,}".format(high_grade)
        self.high_grade_image = self.font.render(high_grade_str, True, self.text_color, self.settings.background_color)

     
        self.high_grade_rect = self.high_grade_image.get_rect()
        self.high_grade_rect.centerx = self.screen_rect.centerx
        self.high_grade_rect.top = self.grade_rect.top

    def level(self):
        self.level_image = self.font.render(str(self.states.level), True, self.text_color, self.settings.background_color)

        # Position the level below the grade.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.grade_rect.right
        self.level_rect.top = self.grade_rect.bottom + 10

    def left_player(self):
        # display the chances that player have
        self.players = Group()
        for player_number in range(self.states.player_left):
            player = Player(self.settings, self.screen)
            player.rect.x = 10 + player_number * player.rect.width
            player.rect.y = 10
            self.players.add(player)

    def display_grade(self):
        self.screen.blit(self.grade_image, self.grade_rect)
        self.screen.blit(self.high_grade_image, self.high_grade_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.players.draw(self.screen)
