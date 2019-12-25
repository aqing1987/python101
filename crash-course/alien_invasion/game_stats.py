class GameStats():
    """track game stats"""

    def __init__(self, ai_settings):
        """init stats"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """init stats which may change during game"""
        self.ships_left = self.ai_settings.ship_limit
