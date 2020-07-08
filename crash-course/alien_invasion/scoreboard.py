import pygame.font

class Scoreboard():
    """Class for showing scores"""

    def __init__(self, ai_settings, screen, stats):
        """init attributes for showing scores"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # set font
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare initial score image
        self.prep_score()

    def prep_score(self):
        """make the score to be an image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.ai_settings.bg_color)

        # put the score image to the top-right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """show score image"""
        self.screen.blit(self.score_image, self.score_rect)