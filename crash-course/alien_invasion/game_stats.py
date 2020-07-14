class GameStats():
    """track game stats"""

    def __init__(self, ai_settings):
        """init stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        # the highest score should not be reset
        self.high_score = 0

    def reset_stats(self):
        """init stats which may change during game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
