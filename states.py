class States():

    def __init__(self, settings):
        """ Initialize states  """
        self.settings = settings
        self.renew()
        self.game_active = False
        self.high_grade = 0

    def renew(self):
        # renew states
        self.player_left = self.settings.limit
        self.grade = 0
        self.level = 1
