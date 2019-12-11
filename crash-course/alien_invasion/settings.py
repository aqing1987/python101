class Settings():
    """used to store all configuration"""

    def __init__(self):
        """init game configuration"""
        # screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 1.5
