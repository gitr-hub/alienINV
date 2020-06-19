class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 10
        self.ship_limit = 2

        # Bullet settings
        self.bullet_speed = 8.5
        self.bullet_width = 800
        self.bullet_height = 15
        self.bullet_color = (0, 255, 64)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 4
        self.bullet_speed = 8.5
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

     # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)


        # self.settings = ai_game.settings
        # print(len(self.bullets))

#    def donotrun():
#        """ Dummy Stub to prohibit running script """

#if __name__ == '__main__':
#    donotrun()
#else:
#    pass
