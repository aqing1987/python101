import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """a single alien class"""

    def __init__(self, ai_settings, screen):
        """init alien and set its initial position"""
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # load alien image and set its rec parameter
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # each alien near (0, 0)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store accurate position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw alien at pointed position"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """if alien at screen edge, return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

    def update(self):
        """move alien to left or right"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
