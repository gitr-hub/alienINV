import pygame

class GameStats:
    """
    Track statistics for Alien Invasion.
    """
    def __init__(self, ai_game):
        """
        Initialize statistics.
        """
        self.settings = ai_game.settings
        self.reset_stats()
        """
        Start game in an inactive state.
        """
        self.game_active = False
        """
        Start Alien Invasion in an active state.
        """
        # self.game_active = True

        """
        Start game in an inactive state.
        """
        # self.game_active = False

        """
        High score should never be reset.
        """
        self.high_score = 0

    def reset_stats(self):
        """
        Initialize statistics that can change during the game.
        """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

        # self.screen_rect = self.screen.get_rect()
        #  self.settings = ai_game.settings
        # self.stats = ai_game.stats

        """
        Font settings for scoring information.
        """
        self.text_color = (255, 255, 0)
        self.font = pygame.font.SysFont(None, 48)
        """
        Prepare the initial score image.
        """
#        self.prep_score()

