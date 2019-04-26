class Settings():
    """ initialize some basic settings """

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)
        self.limit = 3
        self.bullet_speed = 10
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 100
        self.fleet_drop_speed = 60
        self.speedup = 1
        self.grades = 3
        self.new_settings()

    def new_settings(self):
        # new settings that change during the game
        self.player_speed= 10
        self.bullet_speed = 10
        self.alien_speed = 3
        self.points = 50
        self.direction = 1

    def speedup(self):
        # speed settings and point values
        self.player_speed *= self.speedup
        self.bullet_speed *= self.speedup
        self.alien_speed *= self.speedup
        self.points = int(self.points * self.grades)
